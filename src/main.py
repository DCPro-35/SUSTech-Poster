import os 
from ocr import ocr
from prompt import prompt

INPUT_PATH = "../data/image/input/"
OUTPUT_PATH = "../data/image/output/"
HISTORY_PATH = "../data/image/history/"

def main ():
    #command line interaction
    # Read all the files in the input folder

    # Read the file
    input_file = None
    for file in os.listdir(INPUT_PATH):
        input_file = open(INPUT_PATH+file, "r")

    lang = None

    print("Read file from %s"%input_file)
    while True:
        print("Choose language: 1. Chinese 2. English")
        lang = input()
        if lang == "1":
            lang = "ch"
        elif lang == "2":
            lang = "en"
        else:
            print("Invalid input\n")
            continue
        break

    #ocr
    if lang == "1":
        lang = "ch"
    elif lang == "2":
        lang = "en"

    text = ocr(input_file, lang)

    #generate prompt
    p = prompt(text, lang)

    #move the file to history folder
    os.rename(INPUT_PATH+file, HISTORY_PATH+file)

if __name__ == "__main__":
    main()