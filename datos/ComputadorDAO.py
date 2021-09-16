from datos.Conexion import Conexion
from datos.RatonDAO import RatonDAO
from dominio.Raton import Raton


class ComputadorDAO:

    _INSERTAR = 'INSERT INTO Computador(id_computador, descripcion, id_raton, id_teclado, id_monitor) VALUES (?,?, ?, ?)'
    _SELECCIONAR_RATON = 'select distinct id_computador, nombre, raton, teclado, monitor from Computador'

    @classmethod
    def insertar(cls, computador):
        try:
            with Conexion.obtener_cursor() as cursor:
                valores = (computador.nombre, computador.raton, computador.teclado, computador.monitor)
                cursor.execute(ComputadorDAO._INSERTAR, valores)

                # log.debug(f'Ingreso de persona exitoso: {persona}')
                return cursor.rowcount
        except Exception as e:
            # log.error(f'Error al ingresar la persona: {type(e)}')
            print(e)
            return -1





if __name__ == '__main__':
    #pass
    computadores = ComputadorDAO.seleccionar()
    print(computadores)
    for computador in computadores:
        print(computador)