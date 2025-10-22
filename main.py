#MX
from cesiones_mx.cesion_fisica_a_fisica_mx import generar_cesion_fisica_a_fisica
from cesiones_mx.cesion_fisica_a_moral_mx import generar_cesion_fisica_a_moral
from cesiones_mx.cesion_moral_a_moral_mx import generar_cesion_moral_a_moral
from cesiones_mx.cesion_moral_a_fisica_mx import generar_cesion_moral_a_fisica
#CO
from cesiones_co.cesion_natural_a_natural import generar_cesion_natural_a_natural
from cesiones_co.cesion_natural_a_juridica import generar_cesion_natural_a_juridica
from cesiones_co.cesion_juridica_a_juridica import generar_cesion_juridica_a_juridica
from cesiones_co.cesion_juridica_a_natural import generar_cesion_juridica_a_natural
#ARG
from cesiones_arg.cesion_fisica_a_fisica_arg import generar_cesion_fisica_a_fisica_arg
from cesiones_arg.cesion_fisica_a_juridica_arg import generar_cesion_fisica_a_juridica_arg
from cesiones_arg.cesion_juridica_a_juridica_arg import generar_cesion_juridica_a_juridica_arg
from cesiones_arg.cesion_juridica_a_fisica_arg import generar_cesion_juridica_a_fisica_arg

import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def volver_al_menu():
    input("\nPresiona Enter para volver al menú")

def mostrar_menu():
    print(f"{"*"*10} MENU Q&A {"*"*10}\n")
    print("1. Cesiones MX")
    print("2. Cesiones CO")
    print("3. Cesiones ARG")

def menu_mx():
    print(f"\n{"*"*10} ¿QUE FORMATO VA USAR? {"*"*10} \n")
    print("1. CESIÓN FISICA A FISICA: ")
    print("2. CESIÓN FISICA A JURIDICA: ")
    print("3. CESIÓN JURIDICA A JURIDICA: ")
    print("4. CESIÓN JURIDICA A FISICA: ")
    
    opcion_mx = input("Seleccione una opción: ")
    return opcion_mx

def menu_co():
    print(f"\n{"*"*10} ¿QUE FORMATO VA USAR? {"*"*10} \n")
    print("1. ACTA CESION NATURAL A NATURAL: ")
    print("2. ACTA CESIÓN NATURAL A JURIDICA: ")
    print("3. ACTA CESIÓN JURIDICA A JURIDICA: ")
    print("4. ACTA CESIÓN JURIDICA A NATURAL: ")
    
    opcion_co = input("Seleccione una opción: ")
    return opcion_co

def menu_arg():
    print(f"\n{"*"*10} ¿QUE FORMATO VA USAR? {"*"*10} \n")
    print("1. CESION NATURAL A NATURAL: ")
    print("2. CESIÓN NATURAL A JURIDICA: ")
    print("3. CESIÓN JURIDICA A JURIDICA: ")
    print("4. CESIÓN JURIDICA A NATURAL: ")
    
    opcion_arg = input("Seleccione una opción: ")
    return opcion_arg

def menu():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        
        opcion = input("¿QUÉ PAIS VA A SER?: ")

        if opcion == "1":
            limpiar_pantalla()
            opcion_mx = menu_mx()

            if opcion_mx == "1":
                while True:
                    limpiar_pantalla()
                    generar_cesion_fisica_a_fisica()
                    otro = input("¿Generar otro documento? (s/n): ").lower()
                    if otro != "s":
                        break
            
            elif opcion_mx == "2":
                while True:
                    limpiar_pantalla()
                    generar_cesion_fisica_a_moral()
                    otro = input("¿Generar otro documento? (s/n): ").lower()
                    if otro != "s":
                        break
            
            elif opcion_mx == "3":
                while True:
                    limpiar_pantalla()
                    generar_cesion_moral_a_moral()
                    otro = input("¿Generar otro documento? (s/n): ").lower()
                    if otro != "s":
                        break
                
            elif opcion_mx == "4":
                while True:
                    limpiar_pantalla()
                    generar_cesion_moral_a_fisica()
                    otro = input("¿Generar otro documento? (s/n): ").lower()
                    if otro != "s":
                        break
            
            else:
                print("Opción invalida")
                input("Presiona Enter para continuar...")
        
        elif opcion == "2":
            limpiar_pantalla()
            opcion_co = menu_co()

            if opcion_co == "1":
                while True:
                    limpiar_pantalla()
                    generar_cesion_natural_a_natural()
                    otro = input("¿Generar otro documento? (s/n): ").lower()
                    if otro != "s":
                        break
            
            elif opcion_co == "2":
                while True:
                    limpiar_pantalla()
                    generar_cesion_natural_a_juridica()
                    otro = input("¿Generar otro documento? (s/n): ").lower()
                    if otro != "s":
                        break
            
            elif opcion_co == "3":
                while True:
                    limpiar_pantalla()
                    generar_cesion_juridica_a_juridica()
                    otro = input("¿Generar otro documento? (s/n): ").lower()
                    if otro != "s":
                        break
                
            elif opcion_co == "4":
                while True:
                    limpiar_pantalla()
                    generar_cesion_juridica_a_natural()
                    otro = input("¿Generar otro documento? (s/n): ").lower()
                    if otro != "s":
                        break
            
            else:
                print("Opción invalida")
                input("Presiona Enter para continuar...")
        
        elif opcion == "3":
            limpiar_pantalla()
            opcion_arg = menu_arg()

            if opcion_arg == "1":
                while True:
                    limpiar_pantalla()
                    generar_cesion_fisica_a_fisica_arg()
                    otro = input("¿Generar otro documento? (s/n): ").lower()
                    if otro != "s":
                        break
            
            elif opcion_arg == "2":
                while True:
                    limpiar_pantalla()
                    generar_cesion_fisica_a_juridica_arg()
                    otro = input("¿Generar otro documento? (s/n): ").lower()
                    if otro != "s":
                        break
            
            elif opcion_arg == "3":
                while True:
                    limpiar_pantalla()
                    generar_cesion_juridica_a_juridica_arg()
                    otro = input("¿Generar otro documento? (s/n): ").lower()
                    if otro != "s":
                        break
                
            elif opcion_arg == "4":
                while True:
                    limpiar_pantalla()
                    generar_cesion_juridica_a_fisica_arg()
                    otro = input("¿Generar otro documento? (s/n): ").lower()
                    if otro != "s":
                        break
            
            else:
                print("Opción invalida")
                input("Presiona Enter para continuar...")
        
        else:
            print("Opción invalida")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    menu()