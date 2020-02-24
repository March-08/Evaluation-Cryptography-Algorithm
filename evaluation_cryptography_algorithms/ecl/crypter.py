import os
from datetime import datetime
from random import randrange
import entropy.entropy as entropy

plaintext_path="./crypter_files/plaintext.txt"
encrypted_path="./crypter_files/encrypted.txt"
decrypted_path="./crypter_files/decrypted.txt"

file_index=randrange(10000)

public_key_path="./keys/pubkey"+str(file_index)+".der"
private_key_path="./keys/key"+str(file_index)+".der"


def encrypt_file(plaintext_path):
    start = datetime.now()
    try:
        os.system("openssl rsautl -encrypt -pubin -inkey " + public_key_path +" -in "+ plaintext_path +" -out " +encrypted_path)
        print("file crypted")
    except:
        print ("error to encrypt")
    end = datetime.now()
    time_taken_to_encrypt = end - start
    f=open("./crypter_files/time_to_encrypt.txt","w+")
    f.write(str(time_taken_to_encrypt.total_seconds()))
    f.close()
    #print('Tempo generazione chiave: ', time_taken_to_generate_key.total_seconds())
    return time_taken_to_encrypt.total_seconds()



def decrypt_file(encrypted_path):
    start = datetime.now()
    try:
        os.system("openssl rsautl -decrypt  -inkey " + private_key_path +" -in "+ encrypted_path +" -out " +decrypted_path)
        print("file decrypted")
    except:
        print ("error to decrypt")
    end = datetime.now()
    time_taken_to_decrypt = end - start
    f = open("./crypter_files/time_to_decrypt.txt","w+")
    f.write(str(time_taken_to_decrypt.total_seconds()))
    f.close()
    #print('Tempo generazione chiave: ', time_taken_to_generate_key.total_seconds())
    return time_taken_to_decrypt.total_seconds()



def encrypt_and_decrypt_file(plaintext_path,encrypted_path):
    encrypt_file(plaintext_path)
    decrypt_file(encrypted_path)







if(__name__=="__main__"):
    encrypt_and_decrypt_file(plaintext_path,encrypted_path)




