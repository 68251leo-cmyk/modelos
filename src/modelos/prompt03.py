from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


class Prompt03:
    def __init__(self):
        self.modelo = ChatOllama(model="granite4.1:3b", temperature=0.1)


    def generar_respuestas(self):
        plantilla = ChatPromptTemplate.from_messages([(
            "system",
            """
            Eres un profesor universitario de programacion.
            Instrucciones:
            - responde siempre en español
            - utiliza lenguaje sencillo
            - explica los conceptos paso a paso
            - incluye un ejemplo en python
            - No utilices tecnicismos innecesarios"""
        ),
        (
            "human",
            "Explicame el siguiente tema {tema}"
        )])

        mensajes = plantilla.invoke({"tema":"estructuras condicionales"})
        respuesta = self.modelo.invoke(mensajes)
        return respuesta.content