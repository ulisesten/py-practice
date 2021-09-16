

class Orden:
    contadorOrden = 0
    def __init__(self, computadores):
        Orden.contadorOrden +=1
        self._idOrden = Orden.contadorOrden
        self._computarores = list(computadores)

    def agregar_computadora(self, computador):
        self._computarores.append(computador)

    def __str__(self):
        return f'Orden [idOrden: {self._idOrden}]' \
               f'\n\t{self._computarores[0]}' \
               f'\n\t{self._computarores[1]}'

if __name__=='__main__':
    pass
    # r1 = Raton('USB', 'HP')
    # t1 = Teclado('USB', 'HP')
    # m1 = Monitor('HP', '14')
    # c1 = Computador('HP Pavilon', m1, t1, r1)

    # r2 = Raton('Bluethoo', 'Dell')
    # t2 = Teclado('Bluethoo', 'Dell')
    # m2 = Monitor('Dell', '21')
    # c2 = Computador('Dell', m2,t2, r2)


    # computadoras = [c1,]
    # o1 =  Orden(computadoras)
    # print(o1)
    #
    # o1.agregar_computadora(c2)
    # print(o1)