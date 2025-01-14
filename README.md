pip install pypdfium2 chromadb langchain_community langchain_ollama langchain

requerimientos
ollama
llama3.1

# Chat PDF with IA

Este proyecto es una aplicación de terminal que consiste en un servidor basico de fastApi que permite interactuar y tener conversaciones basadas en la informacion de PDFs. 

## Dependencias utilizadas
- pypdfium2 (lectura de pdfs)
- chromadb (base de datos para almacenar el contexto de los pdfs)
- langchain (framework para facilitar la integración de LLM)
- langchain_community (extension del framework por parte de la comunidad)
- langchain_ollama (permite utilizar langchain con ollama)

## Instalación
1. Clona este repositorio:
   ```bash
   git clone <https://github.com/AgustinM12/Langchain_Chat_fastApi>
   cd Langchain_Chat_fastApi
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

3. Asegúrate de que los recursos (pdfs) estén en el directorio especificado 'pdfs/'.

## Uso
Para ejecutar la aplicación en modo desarrollo:
```bash
uvicorn main:app --reload
```

## Notas importantes
- Debe tener instalado ollama en su PC.
- Por defecto la app usa el modelo de "llama3.1", por lo que debera descargarlo tambien con el comando 'ollama pull llam3.1'.
- Asegurese de tener ollama corriendo en su PC, use el comando 'ollama serve' y puede verificarlo entrando a <http://localhost:11434>.
- para usar otro pdf diferente debe modificar el archivo que se encuentra en el directorio 'helpers/pdf.py', modifique la linea 6 donde se esta importando el archivo. 
