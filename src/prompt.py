import numpy as np

#number of parameters in the prompt
KEYWORD = 5
ABSTRACT = 50
LIMIT = 1950
RANGE = (0,0)
TRAIN_PATH = "/root/vscode/cs330/data/input/Data.txt"

PRESET  = "Please extract %d keywords from the text\
and conclude it to one sentence within %d words. \
Keywords and abstract should use its original language. \
Do not give addtional description. \
Just return a json list in the format\
[{\"keywords\":[xx,...],\"abstract\":\"...\"}]. \
Here's the text: \r\n ["%(KEYWORD, ABSTRACT)

PRESET_CH = "请从以下文本中提取%d个关键词\
    并将其总结为%d个字的摘要。\
        关键字和摘要应使用其原始语言。\
            不要给出附加描述。\
                只需返回格式为\
                    [{\"keywords\":[xx，...],\"abstract\":\"...\"}]的json列表。\
                        以下是文本：\r\n ["%(KEYWORD, ABSTRACT)

def prompt(text, lang):
    #input: prompt, lang
    #output: prompt
    preset = None

    preset_ch = "请从以下文本中提取%d个关键词\
    并将其总结为%d个字的摘要。\
    不要给出任何附加描述。\
    只需给我一个格式为\
    [{\"keywords\":[xx，...],\"abstract\":\"...\"}]的json列表。\
    以下是文本：\r\n ["%(KEYWORD, ABSTRACT)
    
    preset_en  = "Please extract %d keywords from the text\
    Conclude the text to one sentence within %d words. \
    Do not give addtional description. \
    Only give me a json list in the format\
    [{\"keywords\":[xx,...],\"abstract\":\"...\"}]. \
    Here's the text: \r\n ["%(KEYWORD, ABSTRACT)
    
    if lang == "ch":
        preset = preset_ch
    elif lang == "en":
        preset = preset_en
    
    

#geenrate 
def generate_prompt():
    #input: range of the text, (start, end)

    X = np.loadtxt(TRAIN_PATH, dtype=str, delimiter="\t")
    
    #copy the preset
    preset = PRESET

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

#test example
def main():
    print(generate_prompt())
    

    
if __name__ == "__main__":
    main()