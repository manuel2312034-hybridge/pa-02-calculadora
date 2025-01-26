from sumar import sumar
from resta import resta
from multiplicacion import multiplicacion
from dividir import dividir
from suma_avanzada import suma_avanzada

def show_menu():
    print("*"*32)
    print("1. Sumar 2 números")
    print("2. Restar 2 números")
    print("3. Multiplicar 2 números")
    print("4. Dividir 2 números")
    print("5. Sumar N números")
    print("6. Salir")
    print("*"*32)

def main():
    while True:
        show_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"{a} + {b} = {sumar(a,b)}")

        elif opcion == "2":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"{a} - {b} = {resta(a,b)}")

        elif opcion == "3":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"{a} * {b} = {multiplicacion(a,b)}")

        elif opcion == "4":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"{a} / {b} = {dividir(a,b)}")

        elif opcion == "5":
            lista_strings = input("Ingrese los números separados por espacios: ").split()
            numeros = list(map(float, lista_strings))
            print(f"la suma de {numeros} = {suma_avanzada(numeros)}")

        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
