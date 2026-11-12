import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class Contactos:

    def GET(self):

        model_contactos = ModelContactos()

        #almacena en datos los registros recibidos de supabase
        datos = model_contactos.obtenerContactos()
        
        print(model_contactos.obtenerContactos())

        #envia a contactos.html los datos de supabase
        return render.contactos(datos) 