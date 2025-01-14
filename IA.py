from langchain_ollama import OllamaLLM
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = OllamaLLM(model="llama3.2", base_url="http://localhost:11434", temperature=0.8, top_p=0.9, callbacks=[StreamingStdOutCallbackHandler()])

chat_history = []

prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        """Eres una AI llamada Angela, respondes preguntas con respuestas simples ademas debes contestar de vuelta preguntas acorde al contexto """,  
    ),
    
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
])

chain = prompt_template | llm

def chat():
    while True:
        pregunta = input("You: ")
        if pregunta == "adios":
            return
        
        response = chain.invoke({"input": pregunta, "chat_history": chat_history})
        chat_history.append(HumanMessage(content=pregunta))
        chat_history.append(AIMessage(content=response))
        
        print("-"*50)
        
        print("AI:" + response)

chat()