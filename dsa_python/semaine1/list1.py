fruits = ["pomme", "banane", "orange"]
print(fruits[0])  # Accès: O(1)

fruits.append("kiwi")  # Ajout fin: O(1) en moyenne
print(fruits)

fruits.insert(1, "mangue")  # Ajout au milieu: O(n)
print(fruits)

fruits.remove("banane")  # Supprime la valeur : O(n)
print(fruits)

dernier = fruits.pop()  # Retirer dernier : O(1)
print(dernier, fruits)

# Parcours
for fruit in fruits:
    print(fruit)  # O(n)
