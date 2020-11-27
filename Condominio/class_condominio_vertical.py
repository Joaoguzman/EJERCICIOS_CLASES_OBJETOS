#como importar class terreno y condominio ?
from .parent_class_condominio import Terreno, Condominio

class CondominioVertical(Terreno, Condominio):

    def __init__(self, nombre):
        self.nombre = nombre


