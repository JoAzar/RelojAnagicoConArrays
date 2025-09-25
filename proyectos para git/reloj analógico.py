import os
import time

def limpiarPantalla():
    if platform.system() == "Windows":
        os.system("cls");
    else:
        os.system("clear");

def tiempoBorrado():
    time.sleep(1)
    limpiarPantalla();
    

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
for i in range(1, 8):
    for j in range(len(lista)):
        if i==1:
            print(lista[j])
            tiempoBorrado()
        if i==2:
            print(lista[j],"\n",lista[1])
            tiempoBorrado()
        if i==3:
            print(lista[j],"\n",lista[2])
            tiempoBorrado()
        if i==4:
            print(lista[j],"\n",lista[3])
            tiempoBorrado()
        if i==5:
            print(lista[j],"\n",lista[4])
            tiempoBorrado()
        if i==6:
            print(lista[j],"\n",lista[5])
            tiempoBorrado()
    if i==7:
        print("HA PASADO UN MINUTO :D ")
