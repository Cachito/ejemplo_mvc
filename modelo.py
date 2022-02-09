from peewee import *

try:
    db = SqliteDatabase("./db/nivel_avanzado.db")

    class BaseModel(Model):
        class Meta:
            database = db

    class Noticia(BaseModel):
        titulo = CharField(unique=True)
        descripcion = TextField()

        def __str__(self):
            return "El título es: " + self.titulo

    db.connect()
    db.create_tables([Noticia])

except Exception as ex:
    print(f'Excepción: {str(ex)}')

class Modelo:
    def __init__(self):
        print("en modelo")

    def get_datos(self):
        datos = Noticia.select()
        return datos

    def alta(self, titulo, descripcion):
        noticia = Noticia()
        noticia.titulo = titulo
        noticia.descripcion = descripcion

        noticia.save()

    def baja(self, delete_id):
        borrar = Noticia.get(Noticia.id == delete_id)
        borrar.delete_instance()

    def modificar(self, update_id, titulo, descripcion):
        actualizar = Noticia.update(
            titulo=titulo, descripcion=descripcion
        ).where(Noticia.id == update_id)

        actualizar.execute()
