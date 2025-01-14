from fastapi import FastAPI, HTTPException
from services.IA import chain, chat_history, HumanMessage, AIMessage, rag_chain
from schemas.schemas import ChatRequest, ChatResponse

ia_routes = FastAPI()
    
@ia_routes.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    pregunta = request.input

    if pregunta.lower() == "adios":
        raise HTTPException(status_code=200, detail="Conversación terminada")

    # Generar contexto relevante
    rag_info = rag_chain(pregunta)

    # Combinar la pregunta con el contexto relevante
    combined_input = f"{pregunta} {rag_info}"

    # Invocar el modelo con el historial y el contexto
    response = chain.invoke({"input": combined_input, "chat_history": chat_history})

    # Actualizar el historial de conversación
    chat_history.append(HumanMessage(content=pregunta))
    chat_history.append(AIMessage(content=response))

    return {
        "response": response,
        "chat_history": [msg.content for msg in chat_history]
    }