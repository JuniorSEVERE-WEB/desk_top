def convert(sentence):
    answers = {"42", "forty two", "forty-two"}
    s = sentence .lower().strip()
    return s in answers 

def main():
    text = input("What is the answer to the great question of life, the universe, and everything?: ")
    print("Yes" if convert(text) else "No")

main()    