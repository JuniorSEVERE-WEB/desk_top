
def make_division(num, deno):
    try:
        return num / deno 
    except ZeroDivisionError:
        print("Error : you cannot divide by 0")
        return None 

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Error: please type a valid number.")


def main():
    x = get_number("Enter x: ")
    y = get_number("Enter a y: ")

    result  = make_division(x, y)

    if result is not None:
        print(f"Result: {result}")
main()