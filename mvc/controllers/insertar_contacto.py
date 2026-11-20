import os
import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class InsertarContacto:

    #renderiza el archivo insertar_contacto.html
    def GET(self):
        return render.insertar_contacto()

    #Recibe los input del formulario y accede a cada uno
    #utilizando el atributo 'name'
    def POST(self):
        #accede a los datos del formulario contactos
        formulario = web.input(foto = {})
        #obtiene el valor del input nombre
        nombre = formulario['nombre']
        #obtiene el valor del input email
        email = formulario['email']
        #obtiene el valor del input telefono
        telefono = formulario['telefono']

        archivo = formulario['foto']
        foto = archivo.filename

        ruta = os.path.join("static/images/",foto)
        with open(ruta, "wb") as file:
            file.write(formulario.foto.file.read())

        #inserta el contacto en la base de datos de Supabase
        model_contactos = ModelContactos()

        datos = model_contactos.insertarContacto(nombre,email,telefono,foto)

        html = """
            <h1>Contacto almacenado correctamente</h1>
            <a href='/contactos'>Regresar</a>
        """
        #indica al navegador que la respuesta es una pagina HTML
        web.header('Content-Type', 'text/html; charset=utf-8')
        return html