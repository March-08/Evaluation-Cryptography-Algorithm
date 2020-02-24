import blowfish2.blowfish_generator
import os
from datetime import datetime
import random
import subprocess

def encrypt_file(plaintext_path,key,iv):
    start = datetime.now()
    print("i")
    try:
        print("ciao")
        os.system("openssl enc -salt -bf -in {} -out crypter_files/encrypted.txt -K {} -iv {}".format(plaintext_path , key, iv))
        print("file crypted")
    except:
        print ("error to encrypt")
    end = datetime.now()
    time_taken_to_encrypt = end - start
    f=open("crypter_files/time_to_encrypt.txt","w+")
    f.write(str(time_taken_to_encrypt.total_seconds()))
    f.close()
    return time_taken_to_encrypt.total_seconds()




def decrypt_file(encrytped_path,key,iv):
    start = datetime.now()
    try:
        output = subprocess.check_output("openssl enc -bf -d -in {}  -K {} -iv {}".format(encrytped_path,key,iv), shell=True)
        output = output.decode("utf-8").strip()
        f=open("crypter_files/decrypted.txt","w+")
        f.write(output)
        f.close()
        print("file decrypted")
    except:
        print("error to decrypt")
    end = datetime.now()
    time_taken_to_decrypt = end - start
    f = open("crypter_files/time_to_decrypt.txt", "w+")
    f.write(str(time_taken_to_decrypt.total_seconds()))
    f.close()
    return time_taken_to_decrypt.total_seconds()


if __name__ =="__main__":
    encrypt_file("crypter_files/plaintext.txt","813BA29BB204A168C474E3F6A89429106324395826DBE780449F41CFC4BB4664","00517E11F40333B438C7C77D1D45C34F")
    decrypt_file("crypter_files/encrypted.txt","813BA29BB204A168C474E3F6A89429106324395826DBE780449F41CFC4BB4664","00517E11F40333B438C7C77D1D45C34F")