def get_guess():
    guess = input("Enter your guess: ")
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("Congratulations! You guessed the correct number.")
    else:
        print("that's not correct. Try again!")

if __name__ == "__main__":
    main()