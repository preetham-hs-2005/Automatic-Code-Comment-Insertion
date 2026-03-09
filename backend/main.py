from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from code_parser import parse_and_comment
import uvicorn

app = FastAPI(title="Automatic Code Comment Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str

class CodeResponse(BaseModel):
    commented_code: str

@app.post("/api/generate", response_model=CodeResponse)
def generate_comments(request: CodeRequest):
    commented_code = parse_and_comment(request.code)
    return CodeResponse(commented_code=commented_code)

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
