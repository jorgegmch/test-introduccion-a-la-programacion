import os

def menuCajero():
    print("CAJERO BANCARROTA S.A.\n")
    print("== MENÚ DE OPCIONES ==\n")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("0. Salir\n")
    opcion=input("Digite 0 para salir o ingrese una opción (1-3): ")
    print("-"*60)
    return opcion

saldoInicial=1000+0

def depositarDinero():
    deposito=int(input("\nIngrese el valor que desea depositar: "))
    if deposito > 0:
        nuevoSaldo1=saldoInicial+deposito
        print(f"\nSu saldo actual ahora es de: ${nuevoSaldo1:,}")
        return nuevoSaldo1
    else:
        print("\nPara hacer efectivo su deposito, debe ingresar un valor superior a $0")

def retirarDinero():
    retiro=int(input("\nIngrese el valor que desea retirar: "))
    if retiro > 0:
        nuevoSaldo=retiro-saldoInicial
        print(f"\nSu saldo actual ahora es de: ${nuevoSaldo:,}")
        return nuevoSaldo
    elif retiro > saldoInicial:
        print("\nSaldo insuficiente.")
    else:
        print("\nPara hacer efectivo su retiro, debe ingresar un valor superior a $0")
        
def consultarSaldo():
    pass
    """saldoTotal=
    print(f"La totalidad de su saldo actual es de: {saldoTotal:,}")
    return saldoTotal"""

isActive=True
while isActive:
    os.system("cls" if os.name=="nt" else "clear")
    opcIngresada=menuCajero()

    if opcIngresada=="1":
        consultarSaldo()
        input("\nPresione ENTER para continuar...\n")

    elif opcIngresada=="2":
        depositarDinero()
        input("\nPresione ENTER para continuar...\n")

    elif opcIngresada=="3":
        retirarDinero()
        input("\nPresione ENTER para continuar...\n")
    
    elif opcIngresada=="0":
        print("\nMuchas gracias por usar CAJERO BANCARROTA S.A.\n")
        isActive=False
    
    else:
        print("La opción ingresada no es válida. Intente nuevamente.")
        input("\nPresione ENTER para continuar...\n")