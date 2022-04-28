from operator import truediv
import os
from pydoc import doc  # Limpiar la consola
import random
from xml.dom.minidom import Document  # Sensación de aleatoriedad
import Preguntas.BancoPreguntas

##################### PREGUNTAS DE PRIMER NIVEL #####################

renglones = Preguntas.BancoPreguntas.primerNivel()
n_pregunta = 0
base_de_preguntas = []
cantidadDePreguntas = len(renglones)

preguntaEscogida = []
opciones = []
pregunta = ""
respuesta = ""


#Guardo preguntas en Array base_de_preguntas
for i in range(cantidadDePreguntas):
    if(renglones[i] == ""):
        continue
    base_de_preguntas.append(renglones[i].split("\t"))

# Validar limpiado de consola
def borrarConsola():
    os.system("cls" if os.name == "nt" else "clear")


#Almacenamiento preguntaEscogida, enviando a cada variable
def escogerPregunta(n_pregunta):
    global opciones, respuesta, pregunta

    preguntaEscogida = base_de_preguntas[n_pregunta]
    pregunta = preguntaEscogida[0]
    respuesta = preguntaEscogida[1]
    opciones = preguntaEscogida[1:]
    for i in range(4):
        random.shuffle(opciones)
    # print(opciones)
    return preguntaEscogida

#Opciones
def mostrarPregunta():
    # borrarConsola()
    print()
    print(pregunta)
    print("A)", opciones[0])
    print("B)", opciones[1])
    print("C)", opciones[2])
    print("D)", opciones[3])
    print()

#Captura respuesta de usuario
def capturarRespuesta():
    respuestaUsuario = ""
    opcionesValidas = ["a", "b", "c", "d"]
    while True:
        respuestaUsuario = input("Ingrese su respuesta > ").lower()
        if not (respuestaUsuario in opcionesValidas):
            print("La respuesta no está entre las opciones válidas, vuelva a intentarlo")
            continue
        break
    return opcionesValidas.index(respuestaUsuario)

#Metodo del juego inicio
# def jugar():
#     escogerPregunta(n_pregunta)
#     mostrarPregunta()   
#     if(opciones[capturarRespuesta()]==respuesta):       
#         print("Su respuesta es correcta")
#         input("ENTER PARA CONTINUAR")
#     else:       
#         print("Su respuesta NO es correcta, JUEGO FINALIZADO")
#         input("ENTER PARA SALIR")
        

# Proceso del juego
def jugar():
    n_pregunta = 0
    confirmacion = 0
    while True:
        try:               
            # jugar()
            escogerPregunta(n_pregunta)
            mostrarPregunta()           
            if(opciones[capturarRespuesta()]==respuesta):
                print("Respuesta correcta",respuesta)
                # input("ENTER PARA CONTINUAR")
            else:
                print("Su respuesta NO es correcta, JUEGO FINALIZADO")
                input("ENTER PARA SALIR")
                break        
        except:
            pass
        n_pregunta += 1
        if(n_pregunta==cantidadDePreguntas):            
            borrarConsola()
            print("Primer nivel superado, vamos por mas!")
            valorPremio = 500000
            print("Premio Acomulado $",valorPremio ,"COP")
            confirmacion = int(input("Desea continuar?\n1)SI\n2)NO\n>"))
            if (confirmacion==1):
                print("Buena suerte en la siguiente ronda!")
                input("ENTER PARA CONTINUAR")
                borrarConsola()
                import Niveles.SegundoNivel
                Niveles.SegundoNivel.jugar()
            elif (confirmacion==2):
                print("Premio total > ",valorPremio)
                break
            else:
                print("Opcion no valida, JUEGO FINALIZADO")
                print("Premio total > ",valorPremio)
        
    # return confirmacion



        
            
        