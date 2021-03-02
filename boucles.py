### boucles

# ouvrir un fichier
# open() 2 arguments le fichiers et le mode

f = open("python.txt", "r")
print(f)

# lecture du fichier

g = f.read()
print(g)

# training

h = open("departements_fr.csv", "r", encoding="ISO-8859-1")
data = h.read()

print(data)

#split
"""
names = "Tom,Seb,Fred"
name_split = names.split(",")
print(name_split)

"""
# training

rows = data.split("\n")
# rows_slice = rows[0:5]
print("\n")
print(rows[0:5])

# loop FOR
# exemple
cities = ["Paris", "Madrid", "Rome"]

for city in cities:
    print(city)
    print("\n")


# training

ten_rows = rows[0:10]

for row in ten_rows:
    print(row)


# liste de liste

cities_number = ["Paris,75", "Madrid,33", "Rome,45"]

final_list = [] # creation d'une liste vide

for row in cities_number:
    split_list = row.split(",")
    final_list.append(split_list)

print(final_list)











