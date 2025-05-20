# app/services/inference.py

from app.agents.infra_agent import build_agent

def get_infra_answer(question: str) -> str:
    """
    This is the main interface used by FastAPI or Streamlit to get an answer.
    It runs the LangGraph agent that:
      1. Loads relevant context (Terraform code chunks, tfvars)
      2. Injects them into a structured MCP prompt
      3. Sends to LLaMA via Ollama
      4. Returns the structured answer
    """
    agent = build_agent()

    try:
        result = agent.invoke({"question": question})
        return result["answer"]

    except Exception as e:
        return f"⚠️ Failed to generate answer: {str(e)}"
