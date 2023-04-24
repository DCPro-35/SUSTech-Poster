import numpy as np

#number of parameters in the prompt
KEYWORD = 5
ABSTRACT = 100
LIMIT = 1950
RANGE = (0,2)
TRAIN_PATH = "/root/vscode/cs330/data/input/Data.txt"

BATCH_PRESET = "Please extract %d keywords from each element in the json list\
and conclude it to an abstract within %d words. \
Keywords and abstract should use its original language. \
Each element in the list includes a text.\
Do not give addtional description. \
Just return a json list in the format\
[{\"keywords\":[xx,...],\"abstract\":\"...\"},...]. \
Here's the text: \r\n ["%(KEYWORD, ABSTRACT)

PRESET  = "Please extract %d keywords from the text\
and conclude it to an abstract within %d words. \
Keywords and abstract should use its original language. \
Do not give addtional description. \
Just return a json list in the format\
[{\"keywords\":[xx,...],\"abstract\":\"...\"}]. \
Here's the text: \r\n ["%(KEYWORD, ABSTRACT)

#geenrate 
def generate_prompt():
    #input: range of the text, (start, end)

    X = np.loadtxt(TRAIN_PATH, dtype=str, delimiter="\t")
    
    #copy the preset
    preset = BATCH_PRESET

    for i in range(RANGE[0], RANGE[1]+1):
        if len(preset) + len(X[i]) > LIMIT:
            break

        preset = preset +"{"+  X[i]+ "},"
    #remove the last comma
    preset = preset[:-1]+"]"

    #not exceed the limit
    if len(preset) > LIMIT:
        raise ValueError("Prompt too long")
    return preset

def batch_generate_prompt():

    X = np.loadtxt(TRAIN_PATH, dtype=str, delimiter="\t")
    
    # load all the text to a list
    preset_list = []

    preset = PRESET

    for i in range(0, len(X)):
        
        if len(preset) + len(X[i]) < LIMIT:
            preset = preset +"{"+  X[i]+ "},"
        else:
            #remove the last comma
            preset = preset[:-1]+"]"
            #reach the limit, add to the list and reset the preset
            preset_list.append(preset)
            preset = PRESET

    return preset_list

#test example
def main():
    print(generate_prompt())
    
    print(len(batch_generate_prompt()))
    
if __name__ == "__main__":
    main()