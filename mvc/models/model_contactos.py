import os
from supabase import create_client, Client
from dotenv import load_dotenv
import hashlib
import hmac
from typing import Any, cast
import logging

load_dotenv()

logger = logging.getLogger(__name__)

class ModelContactos:
    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL" , ""),
                os.environ.get("SUPABASE_KEY" , "")
            )
            self.SECRET_KEY = b"chamulhuacan"
        except Exception as error:
            print(f"ERROR 100: {str(error)}")

    def generar_hash(self,id: int) -> str:
        try:
            """Genera un hash único a partir del ID."""
            mensaje = str(id).encode("utf-8")
            firma =  hmac.new(self.SECRET_KEY, mensaje, hashlib.sha256).hexdigest()
            # Concatena el id:firma
            return f"{id}:{firma}"
        except Exception as error:
            print(f"ERROR 106: {str(error)}")
            return ""


    def validar_hash(self,hash_a_validar: str) -> int|None:
        try:
            # Separa el id, separador y la firma
            id_str, sep, _ = hash_a_validar.partition(":")
            resultado_id = None

            # Solo calculamos el hash si la estructura básica es válida
            if sep and id_str.isdigit():
                token_esperado = self.generar_hash(int(id_str))
                if hmac.compare_digest(token_esperado, hash_a_validar):
                    resultado_id = int(id_str)
                else:
                    resultado_id = None
            else:
                resultado_id = None

            return resultado_id
        except Exception as error:
            print(f"ERROR 107: {str(error)}")
            return -1

    def obtenerContactos(self):
        try:
            response = self.supabase.table("contactos").select("*").execute()
            contactos = response.data
            for contacto in contactos:
                contacto["id_contacto"] = self.generar_hash(contacto["id_contacto"])
            return contactos
        except Exception as error:
            logger.error(f"ERROR 200: {str(error)}")
            return []

    def buscarContacto(self, id_contacto: int | str):
        try:
            if isinstance(id_contacto, str) and ":" in id_contacto:
                id_contacto = self.validar_hash(id_contacto)
                if id_contacto is None or id_contacto == -1:
                    return []

            response = self.supabase.table("contactos").select("*").eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 300: {str(error)}")
            return []

    def insertarContacto(self, nombre: str, email: str, telefono: str):
        try:
            response = self.supabase.table("contactos").insert({
                "nombre": nombre,
                "email": email,
                "telefono": telefono
            }).execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 400: {str(error)}")
            return []

    def borrarContacto(self, id_contacto: int | str):
        try:
            if isinstance(id_contacto, str) and ":" in id_contacto:
                id_contacto = self.validar_hash(id_contacto)
                if id_contacto is None or id_contacto == -1:
                    return []

            response = self.supabase.table("contactos").delete().eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 500: {str(error)}")
            return []

    def actualizarContacto(self, id_contacto: int | str, nombre: str, email: str, telefono: str):
        try:
            if isinstance(id_contacto, str) and ":" in id_contacto:
                id_contacto = self.validar_hash(id_contacto)
                if id_contacto is None or id_contacto == -1:
                    return []

            response = self.supabase.table("contactos").update({
                "nombre": nombre,
                "email": email,
                "telefono": telefono
            }).eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 600: {str(error)}")
            return []


if __name__ == "__main__":
    model_contactos = ModelContactos()

    #print(model_contactos.obtenerContactos())
    #print(model_contactos.buscarContacto(1))
    #print(model_contactos.insertarContacto("Carmelo Perez", "carmelo@email.com", "1111234"))
    print(model_contactos.borrarContacto(3))
    print(model_contactos.actualizarContacto(1))
