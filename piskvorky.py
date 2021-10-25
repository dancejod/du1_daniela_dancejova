from turtle import *
from math import *

speed(1)
dlzka = 20
pocet_riadkov = 4
pocet_stlpcov = 4

###Vykresli zadany pocet riadkov
for j in range(pocet_riadkov):
    
    ###Vykresli sestuholnik
    for i in range(6):
        forward(dlzka)
        left(60)
    
    forward(dlzka)
    left(60)
    forward(dlzka)
    right(60)


exitonclick()