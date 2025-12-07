def triangle_right_rev(size):
    for i in range(size):
        spaces = " " * i
        hashes = "#" * (size - i)
        print(spaces + hashes)


def main():
    input_size = int(input("Type your positive number: "))
    triangle_right_rev(input_size)

main()
