


class Monitor:
    contadorMonitor = 0
    def __init__(self, marca, tamano):
        Monitor.contadorMonitor +=1
        self._idMonitor = Monitor.contadorMonitor
        self._marca = marca
        self._tamano = tamano

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self, tamano):
        self._tamano = tamano

    def __str__(self):
        return f'Monitor [idMonitor: {self._idMonitor} Marca: {self._marca} Tamaño: {self._tamano}]'

if __name__ == '__main__':
    m1 = Monitor('HP', '14')
    print(m1)
    m2 = Monitor('Dell', '21')
    print(m2)