import aes.aes_generator
import os
from datetime import datetime
import random
import subprocess


def encrypt_file(plaintext_path,key,iv):

    try:
        start = datetime.now()
       # os.system("openssl enc -nosalt -aes-256-cbc -in {} -out crypter_files_time/encrypted.txt -K {} ".format(plaintext_path , key, iv))
        os.system("openssl enc -nosalt -aes-256-cbc -in {} -out crypter_files_time/encrypted.txt -K {} -iv {}".format(plaintext_path , key, iv))
        print("file crypted")
        end = datetime.now()
        time_taken_to_encrypt = end - start
        print(time_taken_to_encrypt.total_seconds())
        f = open("crypter_files/time_to_encrypt.txt", "w+")
        f.write(str(time_taken_to_encrypt.total_seconds()))
        f.close()
        return time_taken_to_encrypt.total_seconds()
    except:
        print ("error to encrypt")





def decrypt_file(encrytped_path,key,iv):
    try:
        start = datetime.now()
        output = subprocess.check_output("openssl enc -aes-256-cbc -d -in {}  -K {} -iv {}".format(encrytped_path,key,iv), shell=True)
        end = datetime.now()
        time_taken_to_decrypt = end - start
        print(time_taken_to_decrypt.total_seconds())
        output = output.decode("utf-8").strip()
        f=open("crypter_files/decrypted.txt","w+")
        f.write(output)
        f.close()
        print("file decrypted")

        f = open("crypter_files/time_to_decrypt.txt", "w+")
        f.write(str(time_taken_to_decrypt.total_seconds()))
        f.close()
        return time_taken_to_decrypt.total_seconds()
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