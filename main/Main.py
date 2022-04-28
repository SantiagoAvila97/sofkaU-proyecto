
import os

def borrarConsola():
    os.system("cls" if os.name == "nt" else "clear")

documento = int(input("Ingrese su numero de documento > "))
nombre = input("Ingrese sus nombres completos > ").upper()
apellido = input("Ingrese sus apellidos completos > ").upper() 

borrarConsola()


print ("Documento > ",documento)
print ("Usuario > ",nombre,apellido)
print("Por cada categoria aprobada obtendra un +100% de recompensa que la Categoria anterior")

import Niveles.PrimerNivel

Niveles.PrimerNivel.jugar()



