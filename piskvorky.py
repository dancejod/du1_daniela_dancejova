from turtle import *
from math import sqrt

speed(1)
dlzka = 20
pocet_riadkov = 4
pocet_stlpcov = 4

### Vykresli zadany pocet stlpcov
for k in range(pocet_stlpcov):

### Vykresli zadany pocet riadkov
    for j in range(pocet_riadkov):
    
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