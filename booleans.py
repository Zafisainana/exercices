# opérateurs

# == équivalent à
print(1 == 1)
print(2 == 3)

# != différent de
print (8 != 8)
print(8 != 9)


f = open("departements_fr.csv", "r", encoding="ISO-8859-1")

# création de la liste data

data = f.read()

rows = data.split('\n')


final_data=[]
departements = []
int_dep_population = []

for row in rows:
    split_row = row.split(',')

    departements.append(split_row[0])
    int_dep_population.append(int(split_row[1]))

print(departements)
print(int_dep_population)
