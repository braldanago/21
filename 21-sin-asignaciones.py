import random
from random import *

def jugar(mazo, jugador, casa):
    if(len(jugador) < 2 and len(casa) < 2):
       jugar(mazo[2:], repartir([mazo[0]], jugador), repartir([mazo[1]], casa))
       
    #print(jugador)
    #print(casa)
    print("-")
    ordenar(jugador,0,len(jugador))
    ordenar(casa,0,len(casa))
    
    print ("Jugador:")
    print (jugador)
    if (len(casa) <=2):
        print ("Casa:")
        print("##",casa[1:])
    else:
        print ("Casa:")
        print(casa)
    
    if(validarSuma(jugador, 0) > 21):
       print ("Has perdido, tu puntaje: "+ str(validarSuma(jugador,0)))
       print ("Casa:")
       print(casa)
       print ("Puntaje de la casa : "+ str(validarSuma(casa,0)))
       print("----------------------------------")
       exit()
       
    if(validarSuma(jugador, 0) < 21):
        print ("Lleva en total: "+ str(validarSuma(jugador, 0)))
##        print ("Puntaje de la casa: "+ str(validarSuma(casa, 0)))
        if(raw_input("desea continuar s/n: ") != "n"):
            print("----------------------------------")
            jugar(mazo[1:], jugador + [mazo[0]], casa)
        else:
            print ("Has plantado en: " + str(validarSuma(jugador,0)))
            print ("Puntaje de la casa : "+ str(validarSuma(casa, 0)))
            print("--------------------------------- ")
            return jugarMaquina(mazo[1:],casa,validarSuma(jugador,0))
            exit()

    if(validarSuma(jugador, 0) == 21):
        print ("¡Tenemos 21! Esperemos a la casa "+ str(validarSuma(jugador,0)))
        jugarMaquina(mazo[1:],casa,validarSuma(jugador,0))
        print ("Puntaje de la casa: "+ str(validarSuma(casa,0)))
        print("--------------------------------- ")
        exit()
            
    if(validarSuma(casa,0) < 21 ):
        jugarMaquina(mazo[1:],casa,validarSuma(casa,0))
        print("Puntaje de la casa: "+ str(validarSuma(casa,0)))

def jugarMaquina(mazo, casa,numJugador):
    if(validarSuma(casa,0) > 21):
        print ("Casa:")
        print(casa)
        print ("Felicidades , has ganado! ")
        print ("Puntaje de la casa : "+str(validarSuma(casa,0)))
        print ("Tu puntaje es: "+str(numJugador))
        print("----------------------------------")
        exit()
    if(validarSuma(casa,0) >= numJugador and validarSuma(casa,0) <= 21):
        print ("Casa:")
        print(casa)
        print ("¡Vaya, que triste! Gana la casa ")
        print ("Puntaje de la casa : " + str(validarSuma(casa, 0)))
        print ("Tu puntaje es: " + str(numJugador))
        print("----------------------------------")
        exit()
    if(validarSuma(casa,0) < numJugador):
        print ("Casa:")
        print(casa)
        print ("Puntaje de la casa : "+str(validarSuma(casa,0)))
        print("----------------------------------")
        return jugarMaquina(mazo[1:],ordenar(repartir(mazo, casa),0,len(casa)+1),numJugador)
    
def validarSuma(jugador, resultado):
    if(jugador == []):
        return resultado
    else:
        if(jugador[0][0] == "A" and resultado <= 10):
            return (validarSuma(jugador[1:], resultado+11))
        elif(jugador[0][0] == "A" and resultado > 10):
            return (validarSuma(jugador[1:], resultado+1))
        elif(jugador[0][0] == "J" or jugador[0][0] == "Q" or jugador[0][0] == "K"):
            return (validarSuma(jugador[1:], resultado+10))
        else:
            return (validarSuma(jugador[1:], resultado+jugador[0][0]))
   
def repartir(mazo, jugador):
    return jugador + [mazo[0]]

def generarMazo():
    return sample([(x,y) for x in [2,3,4,5,6,7,8,9,10,"J","Q","K","A"] for y in ["p","c","t","d"]],52)

def ordenar(jugador,cont,l):
    if(jugador==[]):
        return jugador

    if(jugador[cont][0]=="A" and cont<(l-1)):
        jugador.extend([jugador[cont]])
        jugador.pop(cont)
        return ordenar(jugador,cont+1,l)
    elif(cont<(l-2)):
        return ordenar(jugador,cont+1,l)
    
    return jugador
    
#jugar(desordenar([(x)for x in [2,3,4,5,6,7,8,9,"A","J","Q","K"]*4] ), [],[])

jugar(generarMazo(),[],[])


