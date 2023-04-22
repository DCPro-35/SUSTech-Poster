#Filter the orginal data, discard the data with too few keywords or abstract
#generate a pair of new data and labels
import numpy as np

TRAIN_PATH = "/root/vscode/cs330/data/input/Train.txt"
TRAIN_LABEL_PATH = "/root/vscode/cs330/data/input/Test.txt"
TRAIN_PATH_NEW = "/root/vscode/cs330/data/input/Data.txt"
TRAIN_LABEL_PATH_NEW = "/root/vscode/cs330/data/input/Label.txt"

def main():
    X = np.loadtxt(TRAIN_PATH, dtype=str, delimiter="\t")
    y = np.loadtxt(TRAIN_LABEL_PATH, dtype=str, delimiter="\t")

    #filter the data
    X_new = []
    y_new = []

    for i in range(0, len(X)):
        y_temp = y[i]
        #split y by comma
        y_temp = y_temp.split("，")
        #text too short or too few keywords
        if len(X[i]) < 50 or len(y_temp) < 2:
            continue
        
        #strip
        y_str = ""
        for j in y_temp:
            y_str = y_str + j.strip() + ","

        #remove the last comma    
        y_str = y_str[:-1]
        
        X_new.append(X[i])
        y_new.append(y_str)
    
    #save the new data
    np.savetxt(TRAIN_PATH_NEW, X_new, fmt="%s", delimiter="\t")
    np.savetxt(TRAIN_LABEL_PATH_NEW, y_new, fmt="%s", delimiter="\t")

if __name__ == "__main__":
    main()