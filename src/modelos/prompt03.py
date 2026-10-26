from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


class Prompt03:
    def __init__(self):
        self.modelo = ChatOllama(model="granite4.1:3b", temperature=0.1)


    def generar_respuestas(self):
        plantilla = ChatPromptTemplate.from_messages([
            "system",
            """
            Eres un profesor universitario de programacion.
            Instrucciones:
            - responde siempre en español
            - utiliza lenguaje sencillo
            - explica los conceptos paso a paso
            - incluye en"""
        ])

        prompt = plantilla.format(tema="inteligencia artificila",nivel="universitario")
        print("Prompt generado: ", prompt)
        respuesta = self.modelo.invoke(prompt)
        print("terminado")
        return respuesta.text