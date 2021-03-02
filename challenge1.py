"""
Ouvrir un fichier
Creer une liste d'entier du nbre des habitants de tous les departement français

ficier departements_fr.csv
"""


# ouverture du fichier

f = open("departements_fr.csv", "r", encoding="ISO-8859-1")

# création de la liste data

data = f.read()

rows = data.split('\n')
print(rows)

final_data=[]
"""
for row in rows:
    split_row = row.split(",")
    final_data.append(split_row)

print(final_data)

department_population = []

for row in final_data:
    dpt_list = int(row[1])
    # dpt_list = row[1]

    department_population.append(dpt_list)

print(department_population)
"""
# ou

for row in rows:
    split_row = row.split(',')
    value = int(split_row[1])
    final_data.append(value)

print(final_data)



