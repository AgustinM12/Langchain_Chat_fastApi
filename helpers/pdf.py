from langchain_community.document_loaders import PyPDFium2Loader
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document

# Cargar el PDF usando PyPDFium2Loader
loader = PyPDFium2Loader("Batman_Hush.pdf")
paginas = loader.load()

# Preprocesamiento de texto para limpiar y estructurar mejor los fragmentos
def preprocess_text(text):
    text = text.replace("\n", " ").strip()  # Eliminar saltos de línea innecesarios
    return text

# Dividir el texto en fragmentos más pequeños
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=400,  # Tamaño más pequeño para fragmentos
    chunk_overlap=50,  # Superposición para mantener contexto
    length_function=len
)

# Preprocesar el texto y crear documentos
docs = [Document(page_content=preprocess_text(page.page_content)) for page in paginas]
docs = text_splitter.split_documents(docs)

# Función para combinar los documentos más relevantes
def combine_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

