def convert(sentence: str) -> str:
    remplacements = {
        ":)": "🙂.",
        ":(": "🙁."
    }
    for old, new in remplacements.items():
        sentence = sentence.replace(old, new)
    return sentence

def main():
    text = input("Type a text: ")
    print(convert(text))

main()    
       