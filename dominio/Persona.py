from PyQt5.QtWidgets import QWidget, QListWidgetItem


class Persona:
    contador_persona=0
    def __init__(self, id_persona=None, nombre=None, apellido=None,
                 cedula=None, email=None, telefono=None):
        Persona.contador_persona += 1
        self._id_persona = Persona.id_persona
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono
        self._email = email
        self._id_persona = id_persona
        self._apellido = apellido

    def __str__(self):
        return f'Persona {self.__dict__}'

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccio = direccion

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

if __name__ == '__main__':
    p1 = Persona('Luis', '0123456789', 'lperez@mail.com', '3698521470')
    print(p1)
