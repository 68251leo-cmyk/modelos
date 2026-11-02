from langchain_ollama import ChatOllama


class ModeloSinMemoria:
    def __init__(self):
        self.modelo = ChatOllama(model="qwen2.5:3b", temperature=0.1)


    def generar_respuestas(self):
        print("-------------------------------------------------\n\nRespuesta a la primera linea\n")
        respuesta = self.modelo.invoke("Mi nombre es Eduardo")
        print(respuesta.text)
        print("--------------------------------------------------\n\nSegudna linea\n")

        respuesta2 = self.modelo.invoke("cual es mi nombre?")
        print(respuesta2.text)
        print("--------------------------------------------------------")