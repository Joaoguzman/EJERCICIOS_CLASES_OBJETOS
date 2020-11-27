
import Condominio as cd

# casa1 = UnidadHabitacional( 1A, 120, ["pepa", "popi", "pancha"], 4)

condominio1 = cd.Condominio("calle 3", ["a", "b" , "c"], 7, 5, ["a", "b"],
                        ["a", "b"], ["1", "2", "3"], 999)
guardia1 = cd.Guardia("joao", "guzman", "19124333-1", "las brisas")
guardia2 = cd.Guardia("joao", "guzman", "19124333-3", "las brisas")

condominio1.agregar_guardia(guardia1)
condominio1.agregar_guardia(guardia2)
condominio1.del_guardia("19124333-1")
print(condominio1.lista_guardias)
for guardia in condominio1.lista_guardias:
    print(guardia.rut)
condominio1.agregar_personal_mantenimiento("Daniela Corvalan")

condominio1.imprimir_lista_personal()

guardia1.comenzar_turno()
guardia1.terminar_turno()

guardia1.ver_registro(entrada=True, salida=True)

terreno1 = cd.Terreno("Av. mar #14656", 10000, "Regado R1", "Habitacional", 10000000, "573-26")

print(terreno1.get_rol())
print(terreno1.get_potencial_terreno())
terreno1.set_potencial_terreno("Agricola")
print(terreno1.get_potencial_terreno())

