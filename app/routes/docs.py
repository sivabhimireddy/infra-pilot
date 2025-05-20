from fastapi import APIRouter
from app.agents.infra_agent import build_agent

import os
from datetime import datetime

router = APIRouter()

@router.post("/generate")
def generate_docs():
    agent = build_agent()
    question = "Please generate Markdown documentation for this Terraform codebase. Format it with H2 headers per resource/module and bullet points for key settings."

    result = agent.invoke({"question": question})
    doc_text = result["answer"]

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_path = f"docs_output/infra-doc-{timestamp}.md"

    os.makedirs("docs_output", exist_ok=True)
    with open(output_path, "w") as f:
        f.write(doc_text)

    return {"status": "✅ Docs generated", "file": output_path}
