def make_division(num, deno):
    try:
        z = num / deno
    except ValueError:
        print("please type only number")
    except ZeroDivisionError:
        print("please don't type 0 in deno")   
    return z 

def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    display = make_division(x, y)
    print(display)
        
main()     