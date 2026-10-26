#pip insall logchain_ollama
from langchain_ollama import ChatOllama

class ModeloLocal:
    def __init__(self):
        self.modelo = ChatOllama(model="qwen2.5:3b", temperature=0.1)

    def generar_respuestas(self, prompt):
        respuesta = self.modelo.invoke(prompt)
        return respuesta.text