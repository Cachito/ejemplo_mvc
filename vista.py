from tkinter import StringVar
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import Radiobutton
from modelo import Modelo
from tkinter import ttk
from clases.tktemas import Temas


class Ventanita:
    def __init__(self, window):
        self.root = window
        self.root.title("Tarea Poo")

        self.var_titulo = StringVar()
        self.var_descripcion = StringVar()
        self.opcion = StringVar()

        self.modelo = Modelo()

        # Frame
        self.frame = Frame(self.root)
        self.frame.config(width=1020, height=1020)
        self.frame.grid(row=10, column=0, columnspan=4)

        self.tree = ttk.Treeview(self.frame)

        # Etiquetas
        self.lbl_superior = Label(
            self.root, text="Ingrese sus datos", bg="orchid", fg="white", width=40
        )
        self.lbl_titulo = Label(self.root, text="Titulo")
        self.lbl_descripcion = Label(self.root, text="Descripcion")
        self.lbl_registros = Label(
            self.root, text="Mostrar registros existentes", bg="grey", width=40
        )
        self.lbl_temas = Label(
            self.root,
            text="Temas",
            bg="black",
            fg="red",
            height=1,
            width=40,
        )

        self.lbl_superior.grid(
            row=0, column=0, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )
        self.lbl_titulo.grid(row=1, column=0, sticky="w")
        self.lbl_descripcion.grid(row=2, column=0, sticky="w")
        self.lbl_registros.grid(
            row=3, column=0, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )
        self.lbl_temas.grid(
            column=0, row=20, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )

        # Entradas
        self.ent_titulo = Entry(self.root, textvariable=self.var_titulo)
        self.ent_titulo.grid(row=1, column=1)
        self.ent_descripcion = Entry(self.root, textvariable=self.var_descripcion)
        self.ent_descripcion.grid(row=2, column=1)

        # Frame Unidad 4
        self.frame_rojo_izq = Frame(self.root, width="200", height="80", bg="red")
        self.frame_negro = Frame(self.root, width="80", height="80", bg="black")
        self.frame_rojo_der = Frame(self.root, width="200", height="80", bg="red")

        self.frame_rojo_izq.grid(column=0, row=21)
        self.frame_negro.grid(column=1, row=21)
        self.frame_rojo_der.grid(column=2, row=21)

        # Botones
        self.boton_alta = Button(self.root, text="Alta", command=lambda: self.alta())
        self.boton_alta.grid(row=6, column=0)

        self.boton_editar = Button(
            self.root, text="Actualizar", command=lambda: self.modificar()
        )
        self.boton_editar.grid(row=6, column=1)

        self.boton_borrar = Button(
            self.root, text="Borrar", command=lambda: self.borrar()
        )
        self.boton_borrar.grid(row=6, column=2)

        self.rb_amarillo = Radiobutton(
            self.frame_negro,
            text="Tema Amarillo",
            variable=self.opcion,
            value="01",
            fg="yellow",
            bg="black",
            selectcolor="black",
            command=lambda: Temas.tema_amarillo(self, self.root),
        )
        self.rb_amarillo.grid(column=2, row=21)

        self.rb_blanco = Radiobutton(
            self.frame_negro,
            text="Tema Blanco",
            variable=self.opcion,
            value="02",
            fg="white",
            bg="black",
            selectcolor="black",
            command=lambda: Temas.tema_blanco(self, self.root),
        )
        self.rb_blanco.grid(column=2, row=22)

        self.rb_rojo = Radiobutton(
            self.frame_negro,
            text="Tema Rojo",
            variable=self.opcion,
            value="03",
            fg="red",
            bg="black",
            selectcolor="black",
            command=lambda: Temas.tema_rojo(self, self.root),
        )
        self.rb_rojo.grid(column=2, row=23)

        # Tree
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Título")
        self.tree.heading("col2", text="Descripción")
        self.tree.heading("col3", text="Mensaje")
        self.tree.grid(row=10, column=0, columnspan=4)

    def alta(self):
        titulo = self.var_titulo.get()
        descripcion = self.var_descripcion.get()

        if not titulo or not descripcion:
            print("Debe completar todos los datos.")
        else:
            self.modelo.alta(titulo, descripcion)
            self.actualizar()

    def borrar(self):
        focus_item = self.tree.focus()
        row = self.tree.item(focus_item)
        delete_id = row["text"]

        if not delete_id:
            print("Debe seleccionar un registro.")
        else:
            self.modelo.baja(delete_id)
            self.actualizar()

    def modificar(self):
        focus_item = self.tree.focus()
        row = self.tree.item(focus_item)
        update_id = row["text"]

        if not update_id:
            print("Debe seleccionar un registro.")
        else:
            titulo = self.var_titulo.get()
            descripcion = self.var_descripcion.get()

            self.modelo.modificar(update_id, titulo, descripcion)
            self.actualizar()

    def actualizar(self):
        records = self.tree.get_children()

        for element in records:
            self.tree.delete(element)

        datos = self.modelo.get_datos()
        for dato in datos:
            self.tree.insert(
                "",
                0,
                text=dato.id,
                values=(
                    dato.titulo,
                    dato.descripcion,
                    dato
                ),
            )
