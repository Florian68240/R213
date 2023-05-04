pret = int(input("Entrez le montant du prêt ou crédit : "))
taux = float(input("Entrez le taux annuel en % : "))
annees = int(input("Entrez le nombre d'années : "))
#tm = (1+taux/100)**(1/12)-1
tm = taux/12/100
a=(1+tm)**(12*annees)
mens = pret*tm*a/(a-1)
print(f"La mensualité avec intérêts est de {round(mens, 2)} euros.")
restant = pret
intremb = 0
for i in range(1, annees*12+1):
    interets = tm*restant
    intremb += interets
    capremb = mens - interets
    restant -= capremb
print(f"Le montant des intérêts remboursés est de {round(intremb,2)}")
print(f"Le taux mensuel est de {round(tm, 4)}")
print("Tableau d'amortiessement :\nMois  -  Mensualité  -  Intérêts  -  Capital remboursé  -  Capital restant dû  -  Intérêts remboursés")
restant = pret
intremb = 0
for i in range(1, annees*12+1):
    interets = tm*restant
    intremb += interets
    capremb = mens - interets
    restant -= capremb
    print(f" {i}    -   {round(mens, 2)}     -   {round(interets, 2)}    -        {round(capremb, 2)}       -       {round(restant, 2)}       -        {round(intremb, 2)}")