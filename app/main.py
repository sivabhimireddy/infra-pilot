from fastapi import FastAPI
from app.routes.ask import router as ask_router
from dotenv import load_dotenv
import os
from app.routes.docs import router as docs_router


# Load environment variables from .env file
load_dotenv()

# Optional: Print confirmation
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file or environment variables.")

# Initialize FastAPI app
app = FastAPI(
    title="Infra Pilot MCP Server",
    description="An autonomous infra copilot to answer Terraform questions",
    version="0.1.0"
)

# Include routes
app.include_router(ask_router, prefix="/ask")
app.include_router(docs_router, prefix="/docs")
