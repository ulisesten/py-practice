from dominio.Monitor import Monitor
from dominio.Raton import Raton
from dominio.Teclado import Teclado


class Computador:
    contadorComputador = 0

    def __init__(self, nombre=None, monitor=None, teclado=None, raton=None):
        Computador.contadorComputador += 1
        self._idComputador = Computador.contadorComputador
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton


    def __str__(self):
        return f'PC [idPC: {self._idComputador} Nombre:{self._nombre}]' \
               f'\n\t{self._monitor}' \
               f'\n\t{self._teclado}' \
               f'\n\t{self._raton}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton


if __name__=='__main__':
    r1 = Raton('USB', 'HP')
    t1 = Teclado('USB', 'HP')
    m1 = Monitor('HP', '14')
    c1 = Computador('HP Pavilon', m1, t1, r1)
    print(c1)

    # r2 = Raton('PS2', 'Genius')
    # print(r2)

    # c1.raton = r2
    #c1.raton = 'PS2, Genius'

    raton_marca = input('Ingrese la marca del raton: ')
    raton_tipo = input('Ingrese el tipo de entrada para el raton: ')

    r2 = Raton(tipoEntrada=raton_tipo, marca=raton_marca)
    c1.raton = r2


    print(c1)

