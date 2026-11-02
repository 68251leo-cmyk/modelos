from langchain_ollama import ChatOllama
from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)
from langchain_core.messages import messages_to_dict, messages_from_dict
import json


class ModeloPersistencia:
    def __init__(self):
        self.archivo = "context.json"
        self.modelo = ChatOllama(model="qwen2.5:3b", temperature=0.1)
        self.historial = [
            SystemMessage(content="Eres un asistente que responde en español.")
        ]
        self.cargar_historial_json()
        

    
    def aumentar_context_json(self):
        with open(self.archivo, 'w') as f:
            json.dump(messages_to_dict(self.historial), f, ensure_ascii=False, indent=4)
 

    def cargar_historial_json(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                mensajes = messages_from_dict(json.load(f))
                if mensajes:  
                    self.historial = mensajes
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Se creará uno nuevo al guardar el historial.")
        except json.JSONDecodeError:
            print(f"Archivo {self.archivo} vacío o corrupto. Se empezará con un historial nuevo.")

    def generar_respuestas(self):
        while True:
            prompt = input("Usuario: ")
            if prompt.lower() == "salir":
                break
            
            self.historial.append(HumanMessage(content=prompt))
            respuesta = self.modelo.invoke(self.historial)
            print("Asistente:", respuesta.text)
            self.historial.append(respuesta)
            self.aumentar_context_json()
