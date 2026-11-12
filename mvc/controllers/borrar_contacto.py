import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class BorrarContacto:

    def GET(self, id_contacto):
        model_contactos = ModelContactos()
        # busca en supabase el contacto con ese id
        datos = model_contactos.buscarContacto(int(id_contacto))
        # si no existe el contacto, envia una lista vacia para mostrar el mensaje
        if datos == []:
            return render.borrar_contacto([])
        # envia a borrar_contacto.html el primer contacto de la lista
        return render.borrar_contacto(datos[0])

    def POST(self, id_contacto):
        model_contactos = ModelContactos()
        # borra el contacto en supabase
        model_contactos.borrarContacto(int(id_contacto))
        # redirige a la lista de contactos
        raise web.seeother('/contactos')
