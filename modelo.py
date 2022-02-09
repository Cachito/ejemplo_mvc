from peewee import *
from observer.observable import Observable
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

"""
La clase Modelo hereda de Observable. Por esto el objeto creado se puede observar.
Cada método cambia el estado (self.estado) y los informa a los observadores (self.notificar())
que hubiera o hubiese en la lista observadores definida en la clase base (Observable)
"""
class Modelo(Observable):
    def __init__(self):
        self.estado = None

    def get_estado(self):
        return self.estado

    def get_datos(self):
        datos = Noticia.select()

        """
        las dos líneas que siguen solo informan a los observadores
        que hubiera (o hubiese) en la lista.
        em método notificar() también está definido en la clase base
        """
        self.estado = "obteniendo registros."
        self.notificar()

        return datos

    def get_by_titulo(self, titulo):
        query = Noticia.select().where(Noticia.titulo == titulo)
        return query.exists()

    def get_other_by_titulo(self, update_id, titulo):
        query = Noticia.select().where((Noticia.titulo == titulo) & (Noticia.id != update_id))
        return query.exists()

    def alta(self, titulo, descripcion):
        noticia = Noticia()
        noticia.titulo = titulo
        noticia.descripcion = descripcion

        noticia.save()

        """
        las dos líneas que siguen solo informan a los observadores
        que hubiera (o hubiese) en la lista.
        em método notificar() también está definido en la clase base
        """
        self.estado = f"Alta: Título:{titulo}, Descripción:{descripcion}."
        self.notificar()

    def baja(self, delete_id):
        borrar = Noticia.get(Noticia.id == delete_id)
        borrar.delete_instance()

        """
        las dos líneas que siguen solo informan a los observadores
        que hubiera (o hubiese) en la lista.
        em método notificar() también está definido en la clase base
        """
        self.estado = f"Baja: Id:{delete_id}"
        self.notificar()

    def modificar(self, update_id, titulo, descripcion):
        actualizar = Noticia.update(
            titulo=titulo, descripcion=descripcion
        ).where(Noticia.id == update_id)

        actualizar.execute()

        """
        las dos líneas que siguen solo informan a los observadores
        que hubiera (o hubiese) en la lista.
        em método notificar() también está definido en la clase base
        """
        self.estado = f"Modificación: Id:{update_id}, Título:{titulo}, Descripción:{descripcion}."
        self.notificar()
