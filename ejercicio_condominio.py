
import Condominio as cd 

# casa1 = UnidadHabitacional( 1A, 120, ["pepa", "popi", "pancha"], 4)

#condominio1 = cd.Condominio("calle 3", ["a", "b" , "c"], 7, 5, ["a", "b"],
#                        ["a", "b"], ["1", "2", "3"], 999)
#terreno1 = cd.Terreno("Av. mar #14656", 10000, "Regado R1", "Habitacional", 10000000, "573-26")
guardia1 = cd.Guardia("joao", "guzman", "19124333-1", "las brisas")

administradores = ["Juan Peréz","Ana Peréz","Gonzalo Peréz"]

condominio_vertical1 = cd.CondominioVertical("Torres del Mar",
        "Av. mar #14656", 10000, "Regado R1", "Habitacional", 10000000,
        "573-26",administradores,4,10,["Depto-A","Depto-B"],["margarita"],
        ["juan","mario","tomás"],"A001")

condominio_vertical1.agregar_guardia(guardia1)
guardias = condominio_vertical1.get_guardias()
for guardia in guardias:
    print(guardia.nombre)

condominio_vertical1.informacion()
print(condominio_vertical1.get_tipo_unidades())
print(condominio_vertical1.get_total_unidades())