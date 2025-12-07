def triangle_left(size):

    for i in range(1, size + 1):
        print(" " * (size - i) + "#" * i)


def main():
    input_size = int(input("Type your positive number:  "))
    affichage = triangle_left(input_size)
    print(affichage)

main()    