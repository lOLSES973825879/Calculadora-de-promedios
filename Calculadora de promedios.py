#Proyecto para profe de mate

#Variables
Nota = int
consulta = str
Lista1 = []

def promedio (Nota, consulta, Lista1):
    #Bucle while
    while True:
        #Se define el valor de variables
        Nota = int(input("Ingrese una nota: "))
        consulta = str(input("¿Desea ingresar otra nota? (Si/No): "))
        Lista1.append(Nota)
        #Condición 1
        if consulta == "Si":
            Nota = int(input("Ingrese una nota: "))
            consulta = str(input("¿Desea ingresar otra nota? (Si/No): "))
            Lista1.append(Nota)
        #Condición 2
        else:
            print("El promedio de las notas ingresadas", Lista1, "es: ", round(sum(Lista1)/len(Lista1)))
            consulta = str(input("¿Desea calcular otro promedio? (Si/No): "))
            #Se define el valor de variables 2
            if consulta == "Si":
                Lista1 = []
                Nota = int(input("Ingrese una nota: "))
                consulta = str(input("¿Desea ingresar otra nota? (Si/No): "))
                Lista1.append(Nota)
            elif consulta == "No":
                input("Presione enter para salir")
                break
            

#Función 1

promedio (Nota, consulta, Lista1)