from fastapi import FastAPI
from pydantic import BaseModel
from core.orchestrator import BFSIAssistant
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="BFSI Call Center AI Assistant",
    description="Hybrid Deterministic + RAG + Local LLM BFSI Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



assistant = BFSIAssistant()


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    query: str
    response: str
    routing: str


@app.post("/query", response_model=QueryResponse)
def handle_query(request: QueryRequest):

    if not request.query.strip():
        return {
            "query": request.query,
            "response": "Please enter a valid query.",
            "routing": "VALIDATION"
        }

    result = assistant.handle_query(request.query)

    return {
        "query": request.query,
        "response": result["response"],
        "routing": result["routing"]
    }
