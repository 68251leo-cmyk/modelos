from langchain_ollama import ChatOllama

class Prompt01:
    def __init__(self):
        self.modelo = ChatOllama(model="granite4.1:3b", temperature=0.1)

    def generar_respuestas(self):
        respuesta = self.modelo.invoke("Hola como estas")
        return respuesta.text