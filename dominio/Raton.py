from dominio.DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contadorRaton = 0

    def __init__(self, idRaton=None, tipoEntrada=None, marca=None, cantidad_botones=None):

        self._idRaton = idRaton
        self._cant_botones = cantidad_botones


        super().__init__(tipoEntrada, marca)

    @property
    def cant_botones(self):
        return self._cant_botones

    @cant_botones.setter
    def cant_botones(self, cantidad):
        self._cant_botones = cantidad

    @property
    def idRaton(self):
        return self._idRaton

    @idRaton.setter
    def idRaton(self, idRaton):
        self._idRaton = idRaton

    def __str__(self):
        return f'Raton [idRaton: {self._idRaton} {super().__str__()}]'

if __name__=='__main__':
    r1 = Raton('USB', 'HP')
    print(r1)
    r2 = Raton ('Bluethoo','Dell')
    print(r2)