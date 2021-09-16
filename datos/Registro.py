from dominio.Persona import Persona


from datos import Rutas


class Registro:
    @classmethod
    def guardar(cls, objeto, ruta):
        ingreso = False
        try:
            with open(ruta, 'a+', encoding='utf8') as archivo:
                archivo.write(f'\n{objeto.__str__()}')
                ingreso = True
                return ingreso
        except Exception as e:
            print(f'Ocurrió un error: {e}')
            return ingreso

    @classmethod
    def leer(cls, ruta):
        try:
            with open(ruta, 'r+', encoding='utf8') as archivo:
                lineas = archivo.readlines()
                retorno_lista = list()
                for linea in lineas:
                    #USB\n
                    retorno_lista.append(linea.rstrip('\n'))
                return retorno_lista
        except Exception as e:
            print(f'Ocurrió un error: {e}')


if __name__ == "__main__":
    # Registro.leer('C:\\Proyectos\\Python\\POO\\ProyectoPPNoc\\archivos\\entradas.txt')
    # from dominio.Raton import Raton
    p = Persona('Luis', '0258741369', 'luis@mail.com', '0123456789')
    Registro.guardar(p, Rutas.PERSONA)