import base64

def from_base64_to_binary(s,output_file):
    decoded = base64.decodebytes(s.encode("ascii"))
    #newFileByteArray = bytearray(decoded)
    f=open(output_file,"wb")
    f.write(decoded)
    f.close()
    return decoded