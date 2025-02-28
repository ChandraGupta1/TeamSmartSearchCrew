from fastapi import FastAPI
from pydantic import BaseModel
import confluenceUtil as confluence

# Initialize FastAPI
app = FastAPI()
 
class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    confluence_results = confluence.search_confluence(request.question)    
    return {"answer": confluence_results}
