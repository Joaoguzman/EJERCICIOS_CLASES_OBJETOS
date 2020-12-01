#como importar class terreno y condominio ?
from .parent_class_condominio import Terreno, Condominio

class CondominioVertical(Condominio, Terreno):

    def __init__(self, nombre,direccion, administrador,
                num_unidades_habitacionales, banco, numero_cuenta,
                superficie_m2, tipo_superficie, potencial_terreno, valor, rol):
        self.nombre = nombre

        Terreno.__init__(self, direccion, superficie_m2, tipo_superficie,potencial_terreno,valor, rol)
        Condominio.__init__(self, direccion, administrador, num_unidades_habitacionales, banco, numero_cuenta)
        
        #agregar un 6to atributo

    def get_nombre(self):
        return self.nombre

    def get_total_unidades(self):
        return self.num_unidades_habitacionales

    def ver_informacion(self):
        print("Nombre: ", self.nombre)
        print("Administrador: ", self.lista_administrador)
        print("Direccion: ", self.direccion)

