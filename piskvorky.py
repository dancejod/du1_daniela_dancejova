from turtle import *
from math import sqrt

speed(1)
dlzka = 20
pocet_stlpcov = int(input("Zadaj pocet stlpcov: "))
pocet_riadkov = int(input("Zadaj pocet riadkov: "))

### Vykresli zadany pocet riadkov
for k in range(pocet_riadkov):

### Vykresli zadany pocet stlpcov
    for j in range(pocet_stlpcov):
    
        ### Vykresli sestuholnik
        for i in range(6):
            forward(dlzka)
            left(60)
    
        forward(dlzka)
        left(60)
        forward(dlzka)
        right(60)
    
    penup()
    posun = sqrt((dlzka**2)-((dlzka/2)**2))     ## Taznica rovnostranneho trojuholnika
    setpos(0,2*posun*(k+1))                     ## Posun y suradnice o dvojnasobok taznice krat poradie iteracie
    pendown()


exitonclick()