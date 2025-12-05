def convert(sentence:str)->str:
    sentence = sentence.strip().lower()

    mapping = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    for exi, mine in mapping.items():
        if sentence.endswith(exi):
            return mine 
    return "application/octet-stream"

def main():
    text = input(" type your text like that(cat.png or document.PDF, etc...): ")
    print(convert(text))


main()    
    