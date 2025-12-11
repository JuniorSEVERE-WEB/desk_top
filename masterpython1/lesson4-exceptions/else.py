try:
    x = int(input("Nombre : "))
except ValueError:
    print("Pas un nombre.")
else:
    print("Merci ! Vous avez entré :", x)
