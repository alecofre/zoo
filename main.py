from zoo import Zoo
from leon import Leon
from tigre import Tigre
from vaca import Vaca
from conejo import Conejo


import os

def menu(): 
    opcion = -1
    while opcion < 0 or opcion > 5:
        os.system("cls")
        print("Menú: 0071 Zoo")
        print("[1] Agregar animal")
        print("[2] Trasladar animal a otro zoo")
        print("[3] Desplegar información de los animales")
        print("[4] Mostrar los herbívoros")
        print("[5] Mostrar los carnívoros")
        print("[0] Salir")
        try:
            opcion = int(input("Ingrese su opción: "))
        except:
            input("El valor ingresado no parece ser un número...")
        if opcion < 0 or opcion > 5:
            input("Opción ingresada no válida, presione ENTER para continuar...")
    
    return opcion

zoo_uno = Zoo("Nuestro Zoo")
opcion = 1
while opcion > 0:
    opcion = menu()
    if opcion == 1:

        print('Ingreso datos nuevo animal')
        animal_type = "Z"
        while animal_type not in ['A','B','C','D']:
            animal_type = input('Ingrese\n [A]para agregar león\n [B]para agregar tigre\n [C]para agregar vaca\n [D]para agregar conejo\n ').upper()
            if animal_type not in ['A','B','C','D']:
                print('Opción errónea. Pruebe con otra letra')

        nombre = input('Ingrese nombre: ').upper()
        edad = int(input('Ingrese edad del animal:'))
        nivel_salud = int(input('Ingrese nivel de salud: '))
        nivel_felicidad = int(input('Ingrese nivel de felicidad: '))

        if animal_type == 'A':
            melena = input('Tiene melena? [SI/NO]:')
            if melena.upper() == "SI":
                melena = True
            else:
                melena = False
            nuevo_animal = Leon(nombre, edad, nivel_salud, nivel_felicidad, melena)
        elif animal_type == 'B':
            nuevo_animal = Tigre(nombre, edad, nivel_salud, nivel_felicidad)
        elif animal_type == 'C':
            nuevo_animal = Vaca(nombre, edad, nivel_salud, nivel_felicidad)
        elif animal_type == 'D':
            nuevo_animal = Conejo(nombre, edad, nivel_salud, nivel_felicidad)

        if zoo_uno.agregar_animal(nuevo_animal) == True:
            print("Felicitaciones, animal ingresado satisfactoriamente...")
        else:
            print("Lamentamos informar que el animal ya existe en nuestros registros...")
        input('Presione una tecla para continuar...')

    elif opcion == 2:
        print('Ingreso datos para trasladar un animal')
        nombre = input('Ingrese nombre: ').upper()

        if zoo_uno.eliminar_animal(nombre) == True:
            print(f"Felicitaciones, el animal {nombre} ha sido trasladado satisfactoriamente a otro zoo...")
        else:
            print(f"Sorry!! el animal {nombre} no está en nuestros registros...")
        input('Presione una tecla para continuar...')


    elif opcion == 3:
        # print("-"*30, zoo_uno.nombre,   "-"*30)
        # for animal in zoo_uno.lista_animales:
        #     print(animal.display_info())
        zoo_uno.print_all_info()
        input('Presione una tecla para continuar...')

    elif opcion == 4:
        # print("-"*30, zoo_uno.nombre,"HERBIVOROS",   "-"*30)
        # for animal in zoo_uno.listar_herbivoros():
        #     print(animal.display_info())
        zoo_uno.print_herbivoros()
        input('Presione una tecla para continuar...')
        

    elif opcion == 5:
        # print("-"*30, zoo_uno.nombre, "CARNIVOROS",   "-"*30)
        # for animal in zoo_uno.listar_carnivoros():
        #     print(animal.display_info())
        zoo_uno.print_carnivoros()
        input('Presione una tecla para continuar...')
        
