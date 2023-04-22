#Create a container class for each poster

import json
import datetime

TRAIN_PATH = "/root/vscode/cs330/data/input/Train.txt"
TEST_PATH = "/root/vscode/cs330/data/input/Test.txt"
OUTPUT_PATH = "/root/vscode/cs330/data/output/"

class Poster:

    def __init__(self,uid=None, author = None, category = None,title = None,content = None, keywords = None, abstract = None):
        #all the attributes are string
        #necessary attributes
        self.uid = uid
        self.keywords = keywords
        self.abstract = abstract
        self.content = content
        #optional attributes
        self.author = author
        self.category = category
        self.title = title

    def write_to_json(self):

        out_file = OUTPUT_PATH + self.uid + ".json"
        #write to json file
        with open(out_file, 'w') as f:
            json.dump(self.__dict__, f, indent=4)

    #update attributes from a json file
    def read_json():
        pass

#test example
def main():
    poster = Poster(uid = "0001",  content = "hello world", keywords = "auto", abstract = "auto drive")
    poster.write_to_json()
    print("File: "+ poster.uid + ".json created")

if __name__ == "__main__":
    main()