import finanzas as fz
#Clientes institucion 1
cliente1 = fz.Cliente("Maria",10000)
cliente2 = fz.Cliente("Pedro", 10000)
cliente3 = fz.Cliente("Daniela", 10000)
cliente4 = fz.Cliente("Joao", 10000)
#Clientes institucion 2
cliente5 = fz.Cliente("Maria1",10000)
cliente6 = fz.Cliente("Pedro1", 10000)
cliente7 = fz.Cliente("Daniela1", 10000)
cliente8 = fz.Cliente("Joao1", 10000)

scotiabank = fz.Financiera("Scotiabank",100000000, cliente4, cliente2, cliente3)
#print(scotiabank.clientes)
print(cliente1.nombre)
scotiabank.agregar_cliente(cliente1.nombre, cliente1.saldo)
print(scotiabank.clientes)
santander = fz.Financiera("Santander",100000000, cliente5, cliente6, cliente7)
#print(santander.clientes)
print(cliente1.mostrar_saldo)
cliente1.abonar(9000)
print(scotiabank.mis_clientes())
#print(cliente1.mostrar_saldo())
#print(scotiabank.mis_clientes())



#comprueba si se cumple la condicion del 10% 
#agregar cliente retorna true si se cumple la condicion
# false si no se cumple y avisa del error
#if scotiabank.agregar_cliente(maria,10000000):
#    print("Agregado")
#else:
#    print("Error")
#scotiabank.agregar_cliente(juan)
#scotiabank.agregar_cliente(cliente_1)
#Imprimiendo mis clientes
#scotiabank.mis_clientes()

#scotiabank.mis_clientes()

#scotiabank.mostrar_saldo_institucional()