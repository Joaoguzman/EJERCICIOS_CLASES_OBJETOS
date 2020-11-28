class Terreno:

    def __init__(self, direccion, superficie_m2, tipo_superficie, potencial_terreno,
                valor, rol):
        self.direccion = direccion
        self.superficie_m2 = superficie_m2
        self.tipo_superficie = tipo_superficie
        self.potencial_terreno = potencial_terreno
        self.valor = valor
        self.rol = rol

    def get_rol(self):
        return self.rol

    def get_tipo_superficie(self):
        return self.tipo_superficie
    
    def get_superficie_m2(self):
        return self.superficie_m2

    def get_valor(self):
        return self.valor
    
    def get_potencial_terreno(self):
        return self.potencial_terreno

    def set_potencial_terreno(self, nuevo_potencial):
        self.potencial_terreno = nuevo_potencial

    def get_direccion(self):
        return self.direccion