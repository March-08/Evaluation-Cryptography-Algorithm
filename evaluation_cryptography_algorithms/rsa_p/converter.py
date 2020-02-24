import math
from base64 import decodebytes
import base64





def from_base64_to_binary(s,output_file):
    decoded = base64.decodebytes(s.encode("ascii"))
    #newFileByteArray = bytearray(decoded)
    f=open(output_file,"wb+")
    f.write(decoded)
    f.close()
    return decoded



def  binary_contatenate_keys():
    with open('concatenate_keys/out_concat_pvt.txt', 'r') as content_file:
        content = content_file.read().strip()
        from_base64_to_binary(content, "binary_concatenate_keys/binary_concatenate_pvt.txt")
        '''
        binary_pvt_key = from_base64_to_binary(content)
        fout = open("./binary_concatenate_keys/binary_concatenate_pvt.txt", "w+")
        fout.write(binary_pvt_key)
        fout.close()
        '''

    with open('concatenate_keys/out_concat_pbl.txt', 'r') as content_file:
        content = content_file.read().strip()
        from_base64_to_binary(content, "binary_concatenate_keys/binary_concatenate_pbl.txt")
        print("done")

        '''
        binary_pbl_key = from_base64_to_binary(content)
        fout = open("./binary_concatenate_keys/binary_concatenate_pbl.txt", "w+")
        fout.write(binary_pbl_key)
        fout.close()
        '''




