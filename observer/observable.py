class Observable:
    observadores = []

    def agregar(self, observador):
        self.observadores.append(observador)

    def quitar(self, observador):
        self.observadores.remove(observador)

    def notificar(self):
        for observador in self.observadores:
            observador.update()
