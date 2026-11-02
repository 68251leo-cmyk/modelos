from langchain_ollama import ChatOllama
from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)


class ModeloConMemoria:
    def __init__(self):
        self.modelo = ChatOllama(model="qwen2.5:3b", temperature=0.1)
        self.historial = [
            SystemMessage(content="Eres un asistente que responde en español.")
        ]

    def generar_respuestas(self):
        while True:
            prompt = input("Usuario: ")
            if prompt.lower() == "salir":
                break
            
            self.historial.append(HumanMessage(content=prompt))
            respuesta = self.modelo.invoke(self.historial)
            print("Asistente:", respuesta.text)
            self.historial.append(respuesta)