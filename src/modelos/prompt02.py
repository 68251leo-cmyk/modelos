from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


class Prompt02:
    def __init__(self):
        self.modelo=ChatOllama(model="granite4.1:3b", temperature=0.1)

    def generar_respuestas(self):

        plantilla = PromptTemplate.from_template(
            "Explica el concepto de: {tema} "
            "para estudiantes de nivel {nivel} "
            "incluye un ejemplo sencillo"
        )

        prompt = plantilla.format(tema="inteligencia artificila",nivel="universitario")
        print("Prompt generado: ", prompt)
        respuesta = self.modelo.invoke(prompt)
        print("terminado")
        return respuesta.text