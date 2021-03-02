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




