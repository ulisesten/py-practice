from datos.Conexion import Conexion
from dominio.Raton import Raton


class RatonDAO:
    _SELECCIONAR_DISP_ENTRADA = 'SELECT id_tipo_entrada FROM Dispositivo_Entrada where marca = ? and entrada=?'
    _INSERTAR_RATON = 'INSERT INTO raton(cantidad_botones, id_tipo_entrada) VALUES(?, ?)'
    _INSERTAR_DISP_ENTRADA = 'INSERT INTO Dispositivo_Entrada (marca, entrada) VALUES(?, ?)'
    _SELECCIONAR_RATON = 'select distinct id_raton, marca, entrada, cantidad_botones from raton as r inner join Dispositivo_Entrada as d on r.id_tipo_entrada=d.id_tipo_entrada order by marca'
    # _ACTUALIZAR = 'UPDATE personas SET nombre=?, apellido=?, email=?, cedula=? WHERE idPersona=?'
    # _ELIMINAR = 'DELETE FROM personas WHERE idpersona=?'

    @classmethod
    def insertar(cls, raton):
        try:
            with Conexion.obtener_cursor() as cursor:
                valores = (raton.marca, raton.tipoEntrada)
                cursor.execute(RatonDAO._INSERTAR_DISP_ENTRADA, valores)
                cursor.execute(RatonDAO._SELECCIONAR_DISP_ENTRADA, valores)
                id_disp_entrada = cursor.fetchone()[0]
                valores2 = (raton.cant_botones, id_disp_entrada)
                cursor.execute(RatonDAO._INSERTAR_RATON, valores2)
                # log.debug(f'Ingreso de persona exitoso: {persona}')
                return cursor.rowcount
        except Exception as e:
            # log.error(f'Error al ingresar la persona: {type(e)}')
            print(e)
            return -1


    @classmethod
    def seleccionar(cls):
        with Conexion.obtener_cursor() as cursor:
            cursor.execute(cls._SELECCIONAR_RATON)
            registros = cursor.fetchall()
            ratones = []
            for registro in registros:
                # id_persona = registro[0]
                # nombre = registro[1]
                # apellido = registro[2]
                # cedula = registro[3]
                # email = registro[4]
                raton =  Raton(idRaton=registro[0], marca=registro[1], tipoEntrada=registro[2], cantidad_botones=registro[3])
                ratones.append(raton)
            return ratones


if __name__ == '__main__':

    # r = Raton(marca='HP', tipoEntrada='USB', cantidad_botones='3')
    # RatonDAO.insertar(r)



    ratones = RatonDAO.seleccionar()
    print(ratones)
    for raton in ratones:
        print(raton)