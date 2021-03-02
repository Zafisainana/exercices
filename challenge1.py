"""
Ouvrir un fichier
Creer une liste d'entier du nbre des habitants de tous les departement français

ficier departements_fr.csv
"""


# ouverture du fichier

f = open("departements_fr.csv", "r", encoding="ISO-8859-1")

data = f.read()

print(data)
type(data)