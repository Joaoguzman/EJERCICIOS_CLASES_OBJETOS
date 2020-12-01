
import Condominio as cd 

# casa1 = UnidadHabitacional( 1A, 120, ["pepa", "popi", "pancha"], 4)

#condominio1 = cd.Condominio("calle 3", ["a", "b" , "c"], 7, 5, ["a", "b"],
#                        ["a", "b"], ["1", "2", "3"], 999)
#terreno1 = cd.Terreno("Av. mar #14656", 10000, "Regado R1", "Habitacional", 10000000, "573-26")
guardia1 = cd.Guardia("joao", "guzman", "19124333-1", "las brisas")


condominio_vertical1 = cd.CondominioVertical("Las Brisas altas", 
            "Av. mar s/n",["Donald Trump"], 30,"BCI","123456789", 
            10000, "Todo uso","Habitable",100000000, "104-53")

print(condominio_vertical1.get_administrador())

#Imprimir la lista_unidades (numeracion dpto)
dptos = condominio_vertical1.get_unidades()
for dpto in dptos:
    print(dpto.numero_identificador)