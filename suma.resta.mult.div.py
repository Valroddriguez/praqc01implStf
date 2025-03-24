nume1 = int(input("1:"))
nume2 = int(input("2:"))

def suma( num1,num2):
    sumat = num1 + num2
    print(f"La suma es {sumat}")
    

    
def resta( num1,num2):
    resta = num1 - num2
    print(f"La resta es { resta}")
    
def multiplicar( num1,num2):
    multiplicar = num1 * num2
    print(f"La multiplicación es {multiplicar}")
    
def dividir( num1,num2):
    dividir = num1 / num2
    print(f"la division es {dividir}")
    
if __name__ == "__main__":
    suma(nume1,nume2)
    resta(nume1,nume2)
    multiplicar(nume1,nume2)
    dividir(nume1,nume2)
    