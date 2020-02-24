import math
from base64 import decodebytes
import base64




def from_base64_to_binary(s,output_file):
    decoded = base64.decodebytes(s.encode("ascii"))
   # decoded=s

    f = open(output_file, "wb+")
    f.write(decoded)
    f.close()
    return decoded



def  binary_contatenate_keys():
    with open('concatenate_keys/concatenate_keys.pem', 'r') as content_file:
        content = content_file.read().strip().lstrip().rstrip()
        from_base64_to_binary(content, "binary_concatenate_keys/binary_concatenate_key.txt")
        '''
        binary_pvt_key = from_base64_to_binary(content)
        fout = open("./binary_concatenate_keys/binary_concatenate_pvt.txt", "w+")
        fout.write(binary_pvt_key)
        fout.close()
        '''

binary_contatenate_keys()





