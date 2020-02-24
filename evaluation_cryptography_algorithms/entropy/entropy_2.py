import os
import math
from pathlib import Path
import random

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
PARENT_FOLDER = Path(__file__).parent.parent


def evaluate_entropy_from_file_crypted(filename):
    f = open(filename, 'rb')
    li = []
    while (True):
        x = f.read(1)
        if x == b'':
            break
        li.append(chr(int.from_bytes(x, byteorder='big')))
    return shannonForBinary(li, filename)


def evaluate_entropy_from_file_random(filename):
    f = open(filename, 'r')
    li = []
    x = f.read()
    arr = x.split()
    for i in arr:
        print(i)
        li.append(chr(int(i)))
    return shannonForBinary(li, filename)




def shannonForBinary(data,filename):
    '''
    Performs a Shannon entropy analysis on a given block of data.
    '''
    entropy = 0
    if data:
        length = len(data)

        seen = dict(((chr(x), 0) for x in range(0,256)))
        for byte in data:
            seen[byte] += 1
        for x in range(0,256):
            p_x = float(seen[chr(x)]) / length
            if p_x > 0:
                entropy -= p_x * math.log(p_x, 2)
    print("entropy: " + str(entropy/math.log(len(seen),2)))
    return (entropy / math.log(len(seen),2))


#evaluate_entropy_from_file_random(my_random)         #questo è il file di input
#print(evaluate_entropy_from_file_random("../file3.txt"))

if __name__=="__main__":
    print(evaluate_entropy_from_file_random("../Butterfly_files/file50.txt"))
