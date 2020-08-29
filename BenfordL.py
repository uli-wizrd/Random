import numpy as np
import matplotlib.pyplot as plt
from math import *

j = 0
# dat = [13333333,2333,333333,43333,5333,6333,7333,8333,922,234,567,341,179,934,566,12,2445,452]
# dat = [127763,104617,86281,77869,65885,63202,62428,50294,40686,30417,28206,24017,21547,17952,16404,12974,12171,12076,11665,11264,10631,9049,7983,3320,3305,3198,2588,2522,2187,1407,1403,1351]

dat = [9,310,4,37,25,42,770,11,144,430,530,17,320,65,600,260,34,25,3000,350,78,430,52,700,
       88,240,130,111,300,101,820,81,590,124,840,1800,145,101,270,630,82,420,105,180,80,500,
       180,430,126,66,96,220,61,97,200,720,127,170,47,93,360,36,610,130,1400,690,75,570,78,1500,230,
       148,920,55,380,400,65,550,310,79,210,670,460,77,84,84,200,3000,49,540,72,140,220,460,390,58,
       530,1300,400,165,89,160,73,60,77,270,170,140,99,37,520,510,116,310,520,1100,310,460,170,88,
       440,39,1300,59,82,89,150,360,360,110,570,160,35,24,430,77,330,63,40,980,600,240,370,102,39,
       71,170,230,180,200,160,440,170,460,540,730,390,610,260,1600,215,185,88,760,220,420,250,96,
       132,1800,83,124,147,480,820,205,530,340,2600,300,2000,310,85,340,900,250,100,149,150,139,
       410,101,86,48,570,78,540,220,240,370,420,44,340,230,220,53,26,225,86,127,151,45,510,108,
       62,600,99,285,185,101,290,630,215,101,560,160,185,370,102,175,500,530,350,380,1100,190,
       325,81,72,155,120,165,180,1300,440,900,57,185,50,500,73,135,1100,740,200,730,150,235,
       370,475,116,47,210,64,495,27,140,420,260,125,135,880,19,118,390,117,82,2100,112,12,1200,
       420,220,250,130,790,59,115,270,117,29,135,1900,370,97,155,290,130,155,105]



tbt = []

for i in dat:
    j += 1
    while i > 1:
        plead = i/10
        i = plead
        if i < 1:
            lead = plead * 10
            tbt.append(lead)
    if j == len(dat):
        break

vi = []
jj = 0

for ii in tbt:
    jj += 1
    k = trunc(ii)
    vi.append(k)
    if jj == len(tbt):
        break

vU = []
vD = []
vT = []
vC = []
vCi = []
vSe = []
vSi = []
vO = []
vN = []

co = 0
for iii in vi:
    co += 1

    if iii == 1:
        vU.append(iii)

    elif iii == 2:
        vD.append(iii)

    elif iii == 3:
        vT.append(iii)

    elif iii == 4:
        vC.append(iii)

    elif iii == 5:
        vCi.append(iii)

    elif iii == 6:
        vSe.append(iii)

    elif iii == 7:
        vSi.append(iii)

    elif iii == 8:
        vO.append(iii)

    elif iii == 9:
        vN.append(iii)

    if co == len(vi):
        break

frec = []

for p in range(10):

    if p == 1:
        c = len(vU)
        frec.append(c)

    elif p == 2:
        c = len(vD)
        frec.append(c)

    elif p == 3:
        c = len(vT)
        frec.append(c)

    elif p == 4:
        c = len(vC)
        frec.append(c)

    elif p == 5:
        c = len(vCi)
        frec.append(c)

    elif p == 6:
        c = len(vSe)
        frec.append(c)

    elif p == 7:
        c = len(vSi)
        frec.append(c)

    elif p == 8:
        c = len(vO)
        frec.append(c)

    elif p == 9:
        c = len(vN)
        frec.append(c)

else:
    print("Se han guardado los valores")

print("Frecuencia de digitos entre 1 y 9 en la constante, ordenada de menor a mayor [1,9]", frec)

su = 0
for s in frec:
    su += s

porcen = []

for per in frec:
    perc = per/su * 100
    porcen.append(perc)

print(porcen)

xv = [1, 2, 3, 4, 5, 6, 7, 8, 9]


plt.bar(xv, porcen)
plt.title("Ley de Benford para distancia de estrellas a la tierra en AL")
plt.xlabel("Valores entre 1 y 9")
plt.ylabel("Frecuencia de aparición (%)")
plt.show()
