class Terreno:

    def __init__(self, direccion, superficie_m2, tipo_superficie, potencial_terreno,
                valor, rol):
        self.direccion = direccion
        self.__superficie_m2 = superficie_m2
        self.__tipo_superficie = tipo_superficie
        self.__potencial_terreno = potencial_terreno
        self.__valor = valor
        self.__rol = rol

    def get_rol(self):
        return self.__rol

    def get_tipo_superficie(self):
        return self.__tipo_superficie
    
    def get_superficie_m2(self):
        return self.__superficie_m2

    def get_valor(self):
        return self.__valor
    
    def get_potencial_terreno(self):
        return self.__potencial_terreno

    def set_potencial_terreno(self, nuevo_potencial):
        self.__potencial_terreno = nuevo_potencial