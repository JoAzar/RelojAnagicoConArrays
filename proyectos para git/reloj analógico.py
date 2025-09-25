import os
import time
import platform

lista=['''
 _______
|       |
|_______| ''','''
 _______|
|       | ''','''
 ___    
|   |   |
|   |___| ''','''
 _______
|   |   |
|   |   | ''', '''
________
    |    
____|     ''', '''
     ____
|   |    |
|___|    | ''', '''
     ____
|   |    |
|___|____| ''', '''
 _______
|        
|          ''', '''
 ___ ____
|   |    |
|___|____| ''', '''
 ___ ____
|   |     
|___|      ''']

cont = 0

def limpiarPantalla():
	if platform.system() == "Windows":
		os.system("cls");
	else:
		os.system("clear");

def tiempoBorrado():
	time.sleep(1)
	os.system("cls")
	limpiarPantalla();

for i in range(1, 8):
    for j in range(len(lista)):
        if i==1:
            print(lista[j])
            tiempoBorrado()
        if i>=2:
            print(lista[j],"\n",lista[cont])
            tiempoBorrado()
    cont += 1
        
    if i==6:
        print("HA PASADO UN MINUTO :D ")
