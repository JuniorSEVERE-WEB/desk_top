def triangle_left(size):
    result = ""

    for i in range(1, size + 1):
        result += "#" * i + "\n"
    return result


def main():
    input_size = int(input("Type your positive number: "))
    affichage = triangle_left(input_size)
    print(affichage)

main()    