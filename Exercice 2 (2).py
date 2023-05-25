placement= float(input("Entrez le placement de départ : "))
versement=float(input("Entrez le montant du versement annuel en % : "))
taux = float(input("Entrez le taux annuel en % : "))
annees = int(input("Entrez le nombre d'années : "))
banque = placement
for i in range(annees):
    banque += versement
    banque += (1+taux/12/100)

print(f"Le capital acquis avec des intérêts est de {round(banque, 2)} euros au bout de {round(annees)} avec des versements mensuels de {round(versement, 2)} euros ")
print(f"Les intérêts gagné au tax annuel de {round(taux, 2)} % sont de {round(banque - placement - 12*annees*versement, 2)}")
print(f"Sans placement avec intérêts le capital acquis serait de {round(placement + 12*annees*versement)} euros")
