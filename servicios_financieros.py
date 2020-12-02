import finanzas as fz
#Clientes institucion 1
cliente1 = fz.Cliente("Maria",19999, 19123333)
cliente2 = fz.Cliente("Pedro", 10000, 19234543)
cliente3 = fz.Cliente("Daniela", 10000, 495384)
cliente4 = fz.Cliente("Joao", 14500, 485473)
#Clientes institucion 2
#cliente5 = fz.Cliente("Maria1",10000)
#cliente6 = fz.Cliente("Pedro1", 10000)
#cliente7 = fz.Cliente("Daniela1", 10999)
#cliente8 = fz.Cliente("Joao1", 10000)

lista_clientes_1 = [cliente1, cliente2, cliente3, cliente4]
#lista_clientes_2 = [cliente5, cliente6, cliente7, cliente8]

scotiabank = fz.Financiera("Scotiabank",100000000)

for persona in lista_clientes_1:
    scotiabank.agregar_cliente(persona)
    print(f'Se agrego a {persona.nombre_cliente}')

scotiabank.mostrar_saldo_institucional()
scotiabank.eliminar_cliente("19234543")
scotiabank.mostrar_saldo_institucional()

cliente1.girar(999)
cliente3.girar(7600)
cliente1.girar(100)
cliente4.girar(400)

scotiabank.giros_totales()
scotiabank.mostrar_saldo_institucional()

cliente1.abonar(999)
cliente3.abonar(17600)
cliente1.abonar(100)
cliente4.abonar(400)
scotiabank.abonos_totales()

scotiabank.mostrar_saldo_institucional()

#Paso 2
#for persona in lista_cliente:             s_1:
#    scotiabank.agregar_cliente(persona.nombre_cliente, persona.saldo_cliente)
#    print(f'Se agrego a {persona.nombre_cliente}')

#scotiabank.mis_clientes()
#scotiabank.mostrar_saldo_institucional()


#santander = fz.Financiera("Santander",100000000)

#for persona in lista_clientes_2:
#    santander.agregar_cliente(persona.nombre_cliente, persona.saldo_cliente)
#    print(f'Se agrego a {persona.nombre_cliente}')

#santander.eliminar_cliente(cliente7.id)
#santander.mis_clientes()
#santander.mostrar_saldo_institucional()

#santander.eliminar_cliente(cliente7)
#print(cliente1.mostrar_saldo)
#cliente1.abonar(9000)
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