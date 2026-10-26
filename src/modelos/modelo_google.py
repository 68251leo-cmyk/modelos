from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

class ModeloGoogle:
    def __init__(self):
        load_dotenv() # Cargar variables de entorno desde el archivo .env
        self.modelo = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

    def generar_respuesta(self, prompt):
        respuesta = self.modelo.invoke(prompt)
        return respuesta.text