import finanzas as fz

# 1. Crear 2 financieras de la clase Financiera con nombre y saldo inicial de
# $100Millones.

scotiabank = fz.Financiera("Scotiabank",100000000)
bbva = fz.Financiera("BBVA", 100000000)

# 2. Crear 4 clientes por cada financiera.

maria = fz.Cliente("Maria",10000)
juan = fz.Cliente("Juan",10000)
miguel = fz.Cliente("Miguel",10000)
ana = fz.Cliente("Ana",10000)

scotiabank.agregar_cliente(maria)
scotiabank.agregar_cliente(juan)
scotiabank.agregar_cliente(miguel)
scotiabank.agregar_cliente(ana)

julia = fz.Cliente("Julia",10000)
fernando = fz.Cliente("Fernando",10000)
daniela = fz.Cliente("Daniela",10000)
alex = fz.Cliente("Alex",10000)

bbva.agregar_cliente(julia)
bbva.agregar_cliente(fernando)
bbva.agregar_cliente(daniela)
bbva.agregar_cliente(alex)


# 3. Realizar 3 operaciones por cada cliente de distinto tipo (giro, abono).
print("PUNTO 3\n")

bbva.mostrar_saldo_institucional()
print( bbva.clientes[bbva.clientes.index(julia)].mostrar_saldo() )
bbva.clientes[bbva.clientes.index(julia)].abonar(100000)
print( bbva.clientes[bbva.clientes.index(julia)].mostrar_saldo() )

giro = bbva.clientes[bbva.clientes.index(julia)].girar(1000000)
print("Saldo girado: ", giro)
#Actualizando saldo institucional
bbva.saldo_institucional -=giro

bbva.mostrar_saldo_institucional()
print( bbva.clientes[bbva.clientes.index(julia)].mostrar_saldo() )

abono = bbva.clientes[bbva.clientes.index(julia)].abonar(2500000)
#Actualizando saldo institucional
bbva.saldo_institucional += abono

print( bbva.clientes[bbva.clientes.index(julia)].mostrar_saldo() )
bbva.mostrar_saldo_institucional()
# 4. Realizar giros en dos clientes que demuestren que el saldo no puede ser
# menor a -1000000.
print("PARTE 4\n")
#bbva.mostrar_saldo_institucional()
print( bbva.clientes[bbva.clientes.index(julia)].mostrar_saldo() )
print( bbva.clientes[bbva.clientes.index(daniela)].mostrar_saldo() )

bbva.transferir(julia, bbva, daniela, 2610001)

print( bbva.clientes[bbva.clientes.index(daniela)].mostrar_saldo() )
print( bbva.clientes[bbva.clientes.index(julia)].mostrar_saldo() )
#bbva.mostrar_saldo_institucional()
