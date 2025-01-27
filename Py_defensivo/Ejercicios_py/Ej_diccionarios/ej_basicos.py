#!/usr/bin/env python
from termcolor import colored

class dict_ej_basicos:
    def __init__(self,diccionario):
        self.diccionario = diccionario

    def ej_1(self,clave):
        print(colored(f"Ej1 --> Crear y acceder a un diccionario por su clave",'green'))
        print(colored(f"{self.diccionario}",'yellow'))
        return print(self.diccionario[clave])

    def ej_2(self,nueva_clave,nuevo_valor,clave,valor_mod ):
        print(colored(f"\nEj2 --> Agregar y modificar elementos",'green'))
        self.diccionario[f"{nueva_clave}"] = {nuevo_valor}
        self.diccionario[f"{clave}"] = {valor_mod}
        return print(colored(f"{self.diccionario}","yellow"))

    def ej_3(self,clave_a_eliminar):
        print(colored(f"\nEj3--> Elimina una clave del diccionario",'green'))
        del self.diccionario[clave_a_eliminar]
        print(colored(f"Se ha eliminado {clave_a_eliminar} de forma correcta!","light_grey"))

        return print(colored(f"{self.diccionario}","yellow"))
    
    def ej_4(self):
        print(colored(f"\nEj4--> Mostrar en pantalla diccionario --> usar bucle",'green'))
        for clave, valor in self.diccionario.items():
                print(f"{clave}: {valor}")

if __name__ == "__main__":

    #Ej1
    persona = {"nombre":"Joan", "edad":30, "ciudad":"Valencia"}
    ej = dict_ej_basicos(persona)
    ej.ej_1("edad")
    #Ej2 
    ej.ej_2("profesion","profesor","edad",20)
    #Ej3
    ej.ej_3("profesion")
    #Ej4
    ej.ej_4()

