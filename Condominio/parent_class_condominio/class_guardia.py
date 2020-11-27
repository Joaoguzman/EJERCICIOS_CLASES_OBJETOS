#Creación de clases Guardia, UnidadHabitacional, CuentaCorriente con 3 atributos y 4 métodos.
class Guardia:
    def __init__(self, nombre, apellido, rut, nombre_condominio):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.nombre_condominio = nombre_condominio
        self.inicio_jornada = []
        self.fin_jornada = []
        self.registro = {}
        self.registro_visita = []
        
    def comenzar_turno(self):
        # return hora de comienzo de trabajo
        from datetime import datetime
        hoy = datetime.now()
        fecha = str(hoy.day)+"/"+str(hoy.month) +"/"+str(hoy.year)
        hora = str(hoy.hour)+":"+ str(hoy.minute) +":"+ str(hoy.second)
        self.inicio_jornada.append(fecha + " | " +hora)
        list = [hora]
        self.registro[fecha] = list
    
    def terminar_turno(self):
        # return hora de finalizacion de turno y duracion de jornada
        from datetime import datetime
        hoy = datetime.now()
        fecha = str(hoy.day)+"/"+str(hoy.month) +"/"+str(hoy.year)
        hora = str(hoy.hour)+":"+ str(hoy.minute) +":"+ str(hoy.second)
        self.fin_jornada.append(fecha + " | " +hora)
        self.registro[fecha].append(hora)
    
    def ver_registro(self, entrada=False, salida=False):
        # recorrer condominio
        if salida and entrada:
            print("mostrando entra y salida")
            for indice,dia in enumerate(self.registro.items()):
                print(indice," ",dia)
        elif entrada:
            for entrada in self.inicio_jornada:
                print(entrada)
        elif salida:
            print("Mostrando salida")
            for entrada in self.fin_jornada:
                print(entrada)
        else:
            print("debe elegir una entrada")
    
    def registrar_visita(self, nombre_visita, patente):
        # registra visitas entrantes y salientes ( unidad habitacional de destino/origen )
        registro_dia =  nombre_visita + " - " + patente
        self.registro_visita.append(registro_dia)
    
