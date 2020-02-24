import math
from base64 import decodebytes
import base64
import codecs




def from_base64_to_binary(s,output_file):
    decoded = bytes.fromhex(s)
    # decoded=s
    #decoded = base64.b64decode(s.encode('ascii'))
    f = open(output_file, "wb+")
    f.write(decoded)
    f.close()
    return decoded



def  binary_contatenate_keys():
    with open('concatenate_keys/concatenate_keys.pem', 'r') as content_file:
        content = content_file.read().strip()
        from_base64_to_binary(content, "binary_concatenate_keys/binary_concatenate_key.txt")
        '''
        binary_pvt_key = from_base64_to_binary(content)
        fout = open("./binary_concatenate_keys/binary_concatenate_pvt.txt", "w+")
        fout.write(binary_pvt_key)
        fout.close()
        '''







