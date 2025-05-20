from fastapi import APIRouter
from app.models.schema import AskRequest, AskResponse
from app.services.inference import get_infra_answer

router = APIRouter()

@router.post("/", response_model=AskResponse)
def ask_infra(request: AskRequest):
    answer = get_infra_answer(request.question)
    return AskResponse(answer=answer)