from turtle import *
from math import sqrt

speed(0)
dlzka_strany = 20
pocet_stlpcov = int(input("Zadaj pocet stlpcov herneho pola: "))
pocet_riadkov = int(input("Zadaj pocet riadkov herneho pola: "))
vyska = sqrt((dlzka_strany**2)-((dlzka_strany/2)**2))           ## vyska 1 rovnostranneho trojuholnika v sestuholniku

### Vykresli zadany pocet riadkov
for k in range(pocet_riadkov):

### Vykresli zadany pocet stlpcov
    for j in range(pocet_stlpcov):
    
        ### Vykresli sestuholnik
        for i in range(6):
            forward(dlzka_strany)
            left(60)
    
        forward(dlzka_strany)
        left(60)
        forward(dlzka_strany)
        right(60)
    
    penup()
    setpos(0,2*vyska*(k+1))                     ##   posunie korytnacku na vykreslenie dalsieho riadku vyssie
    pendown()

penup()
setpos(0,0)

### Krizik
def krizik():
    pencolor("red")
    left(60)
    pendown()
    forward(10)
    backward(20)
    forward(10)
    left(60)
    forward(10)
    backward(20)
    right(120)
    penup()

### Kruh
def kruh():
    pencolor("blue")
    pendown()
    dot(25)
    pencolor("white")
    dot(18)
    penup()

pensize(5)

max_pocet_tahov = pocet_stlpcov * pocet_riadkov

### Hra
for tah in range(max_pocet_tahov):
    
    if tah%2 == 1:
        hrac = "Hrac 2 (cerveny)"
    else:
        hrac = "Hrac 1 (modry)"

    kontrola = 0
    while kontrola == 0:                                    ### Kontrolny cyklus na vstupy, ak nie su splnene podmienky, hra nepokracuje
    
        riadok = int(input(hrac + ", zadaj cislo riadku pre tvoj tah: "))
        if riadok <= 0 or riadok > pocet_riadkov:
            print(hrac + ", zadal si neplatne cislo riadku")
            continue
        
        stlpec = int(input(hrac + ", zadaj cislo stlpca pre tvoj tah: "))
        if stlpec <= 0 or stlpec > pocet_stlpcov:
            print(hrac + ", zadal si neplatne cislo stlpca")
            continue
            
        kontrola = 1
            
    x_sur = ((stlpec-1)*((3/2)*dlzka_strany))
    y_sur = ((stlpec-1)*vyska+(riadok-1)*2*vyska)

    setx(x_sur+dlzka_strany/2)
    sety(y_sur+vyska)                           ## korekcie zasadia korytnacku do stredu sestuholnika

    if tah%2 == 1:
        krizik()
    else:
        kruh()
        
print("Koniec hry")
exitonclick()