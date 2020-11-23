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

bbva.mostrar_saldo_institucional()
print( bbva.clientes_list[bbva.clientes_list.index(julia)].mostrar_saldo() )
bbva.clientes_list[bbva.clientes_list.index(julia)].abonar(100000)
print( bbva.clientes_list[bbva.clientes_list.index(julia)].mostrar_saldo() )

saldo = bbva.clientes_list[bbva.clientes_list.index(julia)].girar(1000000)
print("Saldo girado: ",saldo)
#se descuenta de saldo institucional al hacer un gira con saldo negativo
if saldo:
    bbva.saldo_institucional = bbva.saldo_institucional + saldo

print( bbva.clientes_list[bbva.clientes_list.index(julia)].mostrar_saldo() )

bbva.mostrar_saldo_institucional()

#bbva.mis_clientes()