import os
from supabase import create_client, Client
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)

class ModelContactos:
    def __init__(self):
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
        except Exception as error:
            logger.error("ERROR 100: {str(error)}")
            print(f"ERROR 100: {error.args[0]}")

    def obtenerContactos(self):
        try:
            response = self.supabase.table("contactos").select("*").execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 200: {str(error)}")

    def buscarContacto(self, id_contacto: int):
        try:
            response = self.supabase.table("contactos").select("*").eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 300: {str(error)}")    

    def insertarContacto(self, nombre: str, email: str, telefono: str):
        try:
            response = self.supabase.table("contactos").insert({
                "nombre": nombre,
                "email": email,
                "telefono": telefono
            }).execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 400: {str(error)}")

    def borrarContacto(self, id_contacto: int):
        try: 
            response = self.supabase.table("contactos").delete().eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 500: {str(error)}")

    def actualizarContacto(self, id_contacto: int, nombre: str, email: str, telefono: str):
        try:
            response = self.supabase.table("contactos").update({
                "nombre": nombre,
                "email": email,
                "telefono": telefono
            }).eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 600: {str(error)}")


if __name__ == "__main__":
    model_contactos = ModelContactos()

    #print(model_contactos.obtenerContactos())
    #print(model_contactos.buscarContacto(1))
    #print(model_contactos.insertarContacto("Carmelo Perez", "carmelo@email.com", "1111234"))
    print(model_contactos.borrarContacto(3))
    print(model_contactos.actualizarContacto(1))