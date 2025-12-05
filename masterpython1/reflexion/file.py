
def convert(sentence):
    if sentence.endswith(".gif"):
        result= "image/gif"
    elif sentence.endswith(".jpg") or sentence.endswith(".jpeg"):
        result= "image/jpeg"
    elif sentence.endswith(".png"):
        result= "image/png"
    elif sentence.endswith(".pdf"):
        result= "application/pdf"
    elif sentence.endswith(".txt"):
        result= "text/plain"
    elif sentence.endswith(".zip"):
        result= "application/zip"
    else:
        result= "application/octet-stream"

    return result    
    
def main():
    text = input("Type a text: ").strip().lower()
    print(convert(text))    

main()    