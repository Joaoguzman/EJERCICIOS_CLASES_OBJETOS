
import Condominio as cd 

# casa1 = UnidadHabitacional( 1A, 120, ["pepa", "popi", "pancha"], 4)

#condominio1 = cd.Condominio("calle 3", ["a", "b" , "c"], 7, 5, ["a", "b"],
#                        ["a", "b"], ["1", "2", "3"], 999)
#terreno1 = cd.Terreno("Av. mar #14656", 10000, "Regado R1", "Habitacional", 10000000, "573-26")
guardia1 = cd.Guardia("joao", "guzman", "19124333-1", "las brisas")


condominio_vertical1 = cd.CondominioVertical("Las Brisas altas", "Av. mar s/n",["Donald Trump"], 30,"BCI","123456789")

print( condominio_vertical1.get_direccion() )

condominio_vertical1.agregar_guardia(guardia1)

print(condominio_vertical1.get_guardias())

#condominio vertical 1 no accede a los métodos de cuenta corriente