def triangle_left(size):
    for i in range(1, size + 1):
        print("#" * i)


def main():
    input_size = int(input("type a positive number: "))
    triangle_left(input_size)

main()    