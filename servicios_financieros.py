import finanzas as fz

maria = fz.Cliente("Maria",10000)

scotiabank = fz.Financiera("Scotiabank",100000000)

#comprueba si se cumple la condicion del 10% 
#agregar cliente retorna true si se cumple la condicion
# false si no se cumple y avisa del error
if scotiabank.agregar_cliente(maria,10000000):
    print("Agregado")
else:
    print("Error")
#scotiabank.agregar_cliente(juan)
#scotiabank.agregar_cliente(cliente_1)
#Imprimiendo mis clientes
#scotiabank.mis_clientes()

scotiabank.mis_clientes()

scotiabank.mostrar_saldo_institucional()