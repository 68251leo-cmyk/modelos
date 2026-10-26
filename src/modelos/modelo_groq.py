# pip install langchain-groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv

class ModeloGroq:
    def __init__(self):
        load_dotenv()
        self.modelo = ChatGroq(model="openai/gpt-oss-20b", temperature=0.7)

    def generar_respuesta(self, prompt):
        respuesta = self.modelo.invoke(prompt)
        return respuesta.text