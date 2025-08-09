import time
import matplotlib
# Utilise un backend web qui peut s'afficher dans VS Code ou navigateur
matplotlib.use('webagg')  
import matplotlib.pyplot as plt

tailles = [1000, 5000, 10000, 50000, 100000, 500000]
temps_append = []
temps_insert = []

for taille in tailles:
    liste = list(range(taille))
    start = time.time()
    liste.append("X")
    temps_append.append(time.time() - start)
    
    liste = list(range(taille))
    start = time.time()
    liste.insert(0, "X")
    temps_insert.append(time.time() - start)

plt.plot(tailles, temps_append, label="Append (O(1))")
plt.plot(tailles, temps_insert, label="Insert début (O(n))")
plt.xlabel("Taille de la liste")
plt.ylabel("Temps en secondes")
plt.legend()
plt.title("Comparaison Append vs Insert")

# Sauvegarde ET affichage
plt.savefig('comparaison_append_vs_insert.png', dpi=300, bbox_inches='tight')
print("Graphique sauvegardé sous 'comparaison_append_vs_insert.png'")
print("Ouverture du graphique dans le navigateur...")
plt.show()
