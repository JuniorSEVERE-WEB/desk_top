def get_positive_int(prompt="Enter a positive number: "):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass
        print("Please enter a positive integer.")


def triangle_left(size):
    for i in range(size):
        for j in range(i + 1):
            print("#", end="")
        print()


def main():
    size = get_positive_int("Type the positive size you want: ")
    triangle_left(size)


main()
