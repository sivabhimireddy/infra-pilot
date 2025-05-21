
from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import HumanMessage
from langchain.chat_models import ChatOllama
from typing import TypedDict
from app.services.embedding import load_code_context
from app.services.parse_tfvars import parse_variables_tf

class AgentState(TypedDict):
    question: str
    code_chunks: str
    tf_vars: str
    answer: str

def retrieve_context(state: AgentState) -> AgentState:
    code = load_code_context("infra")
    tfvars = parse_variables_tf("infra")
    return {
        "question": state["question"],
        "code_chunks": code,
        "tf_vars": tfvars,
        "answer": ""
    }

def generate_response(state: AgentState) -> AgentState:
    llm = ChatOllama(model="llama3")
    prompt_template = open("app/templates/structured_prompt.txt").read()
    filled_prompt = prompt_template.format(
        code_chunks=state["code_chunks"],
        tf_vars=state["tf_vars"],
        user_query=state["question"]
    )

    print("\n----- FILLED PROMPT SENT TO LLaMA -----\n")
    print(filled_prompt)
    print("\n------------------------------------------\n")

    result = llm.invoke([HumanMessage(content=filled_prompt)])
    return {
        **state,
        "answer": result.content
    }

def build_agent():
    graph = StateGraph(AgentState)

    graph.add_node("RetrieveContext", RunnableLambda(retrieve_context))
    graph.add_node("LLMResponder", RunnableLambda(generate_response))

    graph.set_entry_point("RetrieveContext")
    graph.set_finish_point("LLMResponder")
    graph.add_edge("RetrieveContext", "LLMResponder")

    return graph.compile()
