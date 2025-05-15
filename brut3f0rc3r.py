import string
import sys
import numpy as np

letterList = np.array(list(string.ascii_letters))
numberList = np.array(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
symbolList = np.array(["!", "@", "#", "$", "%", "&", "?"])

charList = np.concatenate((letterList, numberList, symbolList))
length = int(sys.argv[1])

bruteStr = np.array([''] * length)

def bruteforcing(length, index):
    if (index == (length - 1)):
        for x in range(len(charList) - 1):
            bruteStr[index] = charList[x]
            print(''.join(bruteStr))
    else:
        for x in range(len(charList) - 1):
            bruteStr[index] = charList[x]
            bruteforcing(length, index + 1)

bruteforcing(length, 0)
