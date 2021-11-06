from turtle import *
from math import sqrt, sin

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
    vyska = sqrt((dlzka**2)-((dlzka/2)**2))     ##   vyska rovnostranneho trojuholnika, DAJ MIMO CYKLU
    setpos(0,2*vyska*(k+1))                     ##   vyska y suradnice o dvojnasobok taznice krat poradie iteracie
    pendown()

penup()
setpos(0,0)

#a, b = int(input("Hrac, zadaj policko vo formate [riadok, stlpec]"))

pensize(5)

hra = -1

riadok = int(input("Zadaj cislo riadku pre tvoj tah: "))
stlpec = int(input("Zadaj cislo stlpca pre tvoj tah: "))
ls = []
ls.append((riadok,stlpec))
print(ls)

x_sur = ((stlpec-1)*((3/2)*dlzka))
y_sur = ((stlpec-1)*vyska+(riadok-1)*2*vyska)

setx(x_sur+dlzka/2)
sety(y_sur+vyska)                           ## fkcia, ktora zasadi korytnacku do stredu sestuholnika

### Krizik
penup()
pencolor("red")
left(60)
pendown()
forward(10)
backward(20)
forward(10)
left(60)
forward(10)
backward(20)

### Kruh
penup()
pencolor("blue")
pendown()
circle(10)

exitonclick()