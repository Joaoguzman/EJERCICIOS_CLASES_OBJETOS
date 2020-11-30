#como importar class terreno y condominio ?
from .parent_class_condominio import Terreno, Condominio

class CondominioVertical(Terreno, Condominio):

    def __init__(self, nombre,
                direccion, superficie_m2, tipo_superficie, potencial_terreno,
                valor, rol, administrador, num_guardias, 
                num_unidades_habitacionales, lista_unidades,
                lista_residentes, lista_personal_mantenimiento, id_condominio):
        self.nombre = nombre

        Terreno.__init__(self, direccion, superficie_m2, tipo_superficie,potencial_terreno,valor, rol)
        
        Condominio.__init__(self, direccion, administrador, num_guardias, 
                num_unidades_habitacionales, lista_unidades,
                lista_residentes, lista_personal_mantenimiento, id_condominio)
        
        #agregar un 6to atributo

    def get_nombre(self):
        return self.nombre

    def get_total_unidades(self):
        return self.num_unidades_habitacionales

    def informacion(self):
        print("Nombre: ", self.nombre)
        print("Administradors: ", self.lista_administrador)
        print("Direccion: ", self.direccion)

