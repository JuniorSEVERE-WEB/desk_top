

def convert(sentence):
    if sentence == "42" or sentence == "forty two" or sentence == "forty-two":
        return True 
    else:
        return False
    
def main():
    text = input("What is the answer to the great question of life, the universe, and everything?: ").strip().lower()
    if convert(text):
        print("Yes")
    else:
        print("No")    

main()        