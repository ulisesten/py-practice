import sys

import pyodbc as bd
from datos.logger_base import log

class Conexion:
    _SERVIDOR = '192.168.195.170'
    _BBDD = 'OrdenesPC'
    _USUARIO = 'ordenes_sql'
    _PASSWORD = '1234'

    _conexion = None
    _cursor = None

    @classmethod
    def obtener_conexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                    cls._SERVIDOR+';DATABASE='+cls._BBDD+';UID='+cls._USUARIO+';PWD=' + cls._PASSWORD)
                log.debug(f'Conexión exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener la conexión: {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtener_cursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtener_conexion().cursor()
                log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor


if __name__ == '__main__':
    Conexion.obtener_conexion()
    Conexion.obtener_cursor()
