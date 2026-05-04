# maVariable = "tp 2 en cours";
# MACONSTANTE = "c'est une constante";

# print(maVariable);
# print(MACONSTANTE);

somme = []

for i in range(2):
    nombre = int(input(f"Entrez un nombre : "))
    somme.append(nombre);

print("La somme des nombres est :", sum(somme));
print(somme);