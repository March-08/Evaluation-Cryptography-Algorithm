'''
Lancia questo programma da BASH con python3
'''


import os
from datetime import datetime
import random
import time
import subprocess


nome_file_chiaro= "file3.txt"  #metti il nome del file senza path

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file_key = os.path.join(THIS_FOLDER, 'key')  #chiave privata in input
my_file_pubkey = os.path.join(THIS_FOLDER, 'pubkey')    #chiave privata in input

my_file_grande_criptato = os.path.join(THIS_FOLDER, 'crypted_'+nome_file_chiaro)     #file in output criptato
my_file_decriptato_grande = os.path.join(THIS_FOLDER, 'decrypted_'+nome_file_chiaro) #file in output decriptato
my_file_prova_grande = os.path.join(THIS_FOLDER, nome_file_chiaro)   #file chiaro in input da criptare




def contaBlocchiE(inputFile):
    numBlocchi=int((os.path.getsize(inputFile))/245)+1
    return numBlocchi

def contaBlocchiD(inputFile):
    numBlocchi=int((os.path.getsize(inputFile))/256)
    return numBlocchi

def crypt_rsa_only(pub_key, large_file_path):
    numBlocchi = contaBlocchiE(large_file_path)
    start =datetime.now()
    out = b''
    for index in range(numBlocchi):
        pipe =subprocess.Popen("dd count=1 skip=" + str(index) + " if=" + large_file_path + " bs=245 | openssl rsautl -pkcs -encrypt -inkey " + pub_key + " -pubin", shell=True, stdout=subprocess.PIPE).stdout
        out += pipe.read()
    #print(str(out))
    end = datetime.now()
    f = open(my_file_grande_criptato, "wb+")
    f.write(out)
    f.close()
    time_taken_to_encrypt = end - start
    print('Tempo per criptare: ', time_taken_to_encrypt.total_seconds())
    f = open("crypter_files_time/time_to_encrypt.txt", "w+")
    f.write(str(time_taken_to_encrypt.total_seconds()))
    f.close()
    return time_taken_to_encrypt.total_seconds()

def decrypt_rsa_only(pvt_key, crypt_file_path):
    numBlocchi = contaBlocchiD(crypt_file_path)
    start =datetime.now()
    out = ""
    for index in range(numBlocchi):
        pipe = os.popen("dd count=1 skip=" + str(index) + " if=" + crypt_file_path + " bs=256 | openssl rsautl -decrypt -inkey " + pvt_key)
        out += pipe.read()
    #print(str(out))
    end = datetime.now()
    f = open(my_file_decriptato_grande, "w+")
    f.write(out)
    f.close()
    time_taken_to_decrypt = end - start
    print('Tempo per decriptare: ', time_taken_to_decrypt.total_seconds())
    f = open("crypter_files_time/time_to_decrypt.txt", "w+")
    f.write(str(time_taken_to_decrypt.total_seconds()))
    f.close()
    return time_taken_to_decrypt.total_seconds()





'''
#CRIPTA E DECRIPTA CON RSA, RICHIAMA DA BASH
crypt_rsa_only(my_file_pubkey+".txt", my_file_prova_grande)
decrypt_rsa_only(my_file_key+".txt", my_file_grande_criptato)

'''
