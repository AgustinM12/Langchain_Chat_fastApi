from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from  IA import chain, chat_history, HumanMessage, AIMessage

app = FastAPI()

class ChatRequest(BaseModel):
    input:str
    
class ChatRequest(BaseModel):
    input:str
    
@app.post("/chat", response_model=ChatRequest)
async def chat(request:ChatRequest):
    pregunta = request.input
    
    if pregunta.lower() == "adios":
        raise HTTPException(status_code=200, detail="Conversacion terminada")
    
    response = chain.invoke({"input": pregunta, "chat_history": chat_history})
    
    # Actualizar el historial de conversación
    chat_history.append(HumanMessage(content=pregunta))
    chat_history.append(AIMessage(content=response))
    
    return {"response": response, "chat_history": [msg.content for msg in chat_history]}
