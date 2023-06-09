# Calcul du diamètre d’un volet roulant autour de son axe lorsque le volet est ouvert

#Question 1 : Combien de lames « entières » sont nécessaires pour le tablier en position fermée ? 2400/36=66.7 donc 67 lames.
#Question 2 : En déduire la longueur à enrouler. 67*40 = 2680 mm.
#Question 3 : Donner l’équation de la suite arithmétique du diamètre « dn » pour le tour « n ».
#Question 4 : En déduire la circonférence parcourue « cn » pour le tour « n »
#Question 5 :Calculer la longueur enroulée « Ln » au tour « n ». Les tours étant entiers, il sera nécessaire de faire une interpolation linéaire pour définir correctement le diamètre selon la longueur enroulée.  (d -186)/ (2680-2507) = (204 - 186) / (3091 - 2507)    d= 191
#Question 6 :En réalité, afin que les attaches du tablier ne soient pas en extension ou tendues lorsqu’il est fermé, on considère que le tablier reste enroulé sur 2 tours. Pour faire simple, ces 2 tours tiennent compte de la distance entre l’axe et les glissières. Calculer la nouvelle longueur « Ln » à enrouler. Conclure.

import math
l = 9
def d(n):
    return (d0+2*l*n)

d0 = int(input("Entrer le diametre de l'axe en mm: "))
n = int(input("Entrer nombre de tours n: "))

L = 0
for i in range (n):
    L = L+math.pi*d(i)
    print("Tour:",i+1,"  - ","Diametre [mm]:",round(d(i+1),1),"     - ","Longueur enrouléée [mm]:",round(L))
print()
print("Calcul de la longueur L par formule :")
c0=math.pi*d(0)
cn=math.pi*d(n-1)
L=(c0+cn)*(n+0)/2
print("Longeur [mm] pour ",n, "tours :",L )