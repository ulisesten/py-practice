from pyodbc import IntegrityError

from datos.Conexion import Conexion
from dominio.Persona import Persona

from datos.logger_base import log


class PersonaDAO:
    _SELECCIONAR = 'SELECT * FROM personas ORDER BY idPersona'
    _SELECCIONAR_CEDULA = 'SELECT idPersona, cedula, nombre, apellido, email FROM personas where cedula = ?'
    _SELECCIONAR_ID = 'SELECT * FROM personas where idpersona = ?'
    _INSERTAR = 'INSERT INTO personas(nombre, apellido, email, cedula) VALUES(?, ?, ?, ?)'
    _ACTUALIZAR = 'UPDATE personas SET nombre=?, apellido=?, email=?, cedula=? WHERE idPersona=?'
    _ELIMINAR = 'DELETE FROM personas WHERE idpersona=?'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtener_cursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                id_persona = registro[0]
                nombre = registro[1]
                apellido = registro[2]
                cedula = registro[3]
                email = registro[4]
                persona =  Persona(id_persona=id_persona, nombre=nombre,
                                   apellido=apellido, email=email, cedula=cedula)
                personas.append(persona)
            return personas

    @classmethod
    def seleccionar_cedula(cls, persona):
        with Conexion.obtener_cursor() as cursor:
            cursor.execute(cls._SELECCIONAR_CEDULA, persona.cedula)
            registro = cursor.fetchone()
            id = registro[0]
            nombre = registro[2]
            apellido = registro[3]
            email = registro[4]
            cedula = registro[1]
            persona =  Persona(id_persona=id, nombre=nombre, apellido=apellido, email=email, cedula=cedula)
            return persona

    def seleccionar_id(cls, persona):
        with Conexion.obtener_cursor() as cursor:
            cursor.execute(cls._SELECCIONAR_ID, persona.id)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                id_persona = registro[0]
                nombre = registro[1]
                apellido = registro[2]
                email = registro[4]
                persona = Persona(id_persona, nombre, apellido, email)
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        try:
            with Conexion.obtener_cursor() as cursor:
                valores =  (persona.nombre, persona.apellido, persona.email, persona.cedula)
                cursor.execute(PersonaDAO._INSERTAR, valores)
                log.debug(f'Ingreso de persona exitoso: {persona}')
                return cursor.rowcount
        except IntegrityError as ie:
            log.error(f'Error al ingresar la persona: {type(ie)}')
            print(f'{type(ie)}')
            return -2
        except Exception as e:
            log.error(f'Error al ingresar la persona: {type(e)}')
            print(f'{type(e)}')
            return -1

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtener_cursor() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.cedula, persona.id_persona)
            cursor.execute(PersonaDAO._ACTUALIZAR, valores)
            log.debug(f'Actualización de persona exitoso: {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtener_cursor() as cursor:
            cursor.execute(PersonaDAO._ELIMINAR, persona.id_persona)
            log.debug(f'Eliminación de persona exitoso: {persona}')
            return cursor.rowcount

if __name__ == '__main__':
    # persona = Persona(cedula='0123477777')
    # personas = PersonaDAO.seleccionar_cedula(persona)
    # # personas = PersonaDAO.seleccionar()
    # print(personas)
    # for persona in personas:
    #     log.debug(persona)
    #     print(persona)

    persona = Persona(nombre='Maria', email='mperez@mail.com', cedula='0123456789', apellido='Perez')
    cantidad_registros = PersonaDAO.insertar(persona)
    print(cantidad_registros)

    # persona = Persona(8, 'Mayra', 'Proaño', 'mproanio@mail.com', '5555')
    # cantidad_registros = PersonaDAO.actualizar(persona)
    # print(cantidad_registros)

    # persona = Persona(5)
    # cantidad_registros = PersonaDAO.eliminar(persona)
    # print(cantidad_registros)