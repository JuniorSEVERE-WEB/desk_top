def triangle_rev(size):
    for i in range(size):
        print("#" * (size - i))

def main():
    input_size = int(input("Type your positive number: "))
    affichage = triangle_rev(input_size)
    print(affichage)

main()    