from langchain_ollama import OllamaLLM
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from helpers.pdf import combine_docs
from helpers.embedding import retriever

# Configuración del modelo
llm = OllamaLLM(
    model="llama3.1",
    base_url="http://localhost:11434",
    temperature=0,
    top_p=0.4,
    callbacks=[StreamingStdOutCallbackHandler()],
)

# Historial del chat
chat_history = []

# Plantilla de prompt mejorada
prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        """Eres una AI llamada Angela, presentate como tal y cuenta cual es tu contexto. Respondes preguntas con respuestas simples y precisas, utilizando el contexto relevante proporcionado.
        Si no encuentras suficiente contexto, indica claramente que no tienes suficiente información.""",
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "Contexto relevante:\n{context}\n\nPregunta: {input}"),
])

# Función de RAG (Retrieval Augmented Generation)
def rag_chain(question):
    retriever_docs = retriever.invoke(question)
    formatted_context = combine_docs(retriever_docs)
    return formatted_context

# Crear la cadena
chain = prompt_template | llm

# Función de chat principal
def chat():
    while True:
        pregunta = input("You: ")
        if pregunta.lower() == "adios":
            print("Angela: ¡Adiós!")
            break
        
        # Obtener el contexto relevante
        contexto_relevante = rag_chain(pregunta)
        if not contexto_relevante:
            contexto_relevante = "No se encontró contexto relevante en el PDF."
        
        # Generar respuesta con el contexto y el historial
        response = chain.invoke({
            "input": pregunta,
            "context": contexto_relevante,
            "chat_history": chat_history,
        })
        
        # Actualizar historial
        chat_history.append(HumanMessage(content=pregunta))
        chat_history.append(AIMessage(content=response))
        
        print("-" * 50)
        print("Angela: " + response)

# Iniciar el chat
chat()
