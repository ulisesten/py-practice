from dominio.DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contadorTeclado = 0

    def __init__(self, tipoEntrada, marca):
        Teclado.contadorTeclado += 1
        self._idTeclado = Teclado.contadorTeclado
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'Teclado [idTeclado: {self._idTeclado} {super().__str__()}]'

if __name__ == '__main__':
    t1 = Teclado('USB', 'HP')
    print(t1)
    t2 = Teclado('Bluethoo', 'Dell')
    print(t2)