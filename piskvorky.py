from turtle import *
from math import *

speed(0)
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
    taznica = sqrt((dlzka**2)-((dlzka/2)**2))     ## Taznica rovnostranneho trojuholnika
    setpos(0,2*taznica*(k+1))                     ## taznica y suradnice o dvojnasobok taznice krat poradie iteracie
    pendown()

penup()
setpos(0,0)

#a, b = int(input("Hrac, zadaj policko vo formate [riadok, stlpec]"))

pensize(5)

riadok = 2
stlpec = 3
segment = (sqrt(dlzka**2-taznica**2))
x_sur = (dlzka+segment)*(stlpec-1)
y_sur = sin(taznica/dlzka)

setx(x_sur)
sety((y_sur/x_sur)*stlpec + (2*taznica*riadok))            ## taznicaie korytnacku do riadku
#setpos((dlzka*b-dlzka,)

### Krizik
penup()
#setpos(dlzka/2, taznica)
pencolor("red")
left(60)
forward(10)
pendown()
forward(10)
backward(20)
forward(10)
left(60)
forward(10)
backward(20)

### Kruh
penup()
setpos(dlzka/2,taznica/2)
pencolor("blue")
pendown()
circle(10)

exitonclick()