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
        formulario = web.input()
        #obtiene el valor del input nombre
        nombre = formulario['nombre']
        #obtiene el valor del input email
        email = formulario['email']
        #obtiene el valor del input telefono
        telefono = formulario['telefono']

        #imprime los datos para verificar que se obtienes los valores
        #de forma correcta
        #print(f"Nombre: {nombre}")
        #rint(f"Email: {email}")
        #print(f"Telefono: {telefono}")

        #inserta el contacto en la base de datos de Supabase
        model_contactos = ModelContactos()

        datos = model_contactos.insertarContacto(nombre,email,telefono)

        html = """
            <h1>Contacto almacenado correctamente</h1>
            <a href='/contactos'>Regresar</a>
        """
        #indica al navegador que la respuesta es una pagina HTML
        web.header('Content-Type', 'text/html; charset=utf-8')
        return html