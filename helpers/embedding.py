from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from helpers.pdf import docs

# Configuración de embeddings con Ollama
embeddings = OllamaEmbeddings(model="llama3.1", base_url="http://localhost:11434")

# Crear el vectorstore usando los documentos preprocesados
vectorstore = Chroma.from_documents(documents=docs, embedding=embeddings)

# Función para buscar documentos más relevantes usando el vectorstore
retriever = vectorstore.as_retriever()

