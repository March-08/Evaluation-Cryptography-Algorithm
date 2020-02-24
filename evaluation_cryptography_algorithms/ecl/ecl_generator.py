import os
from datetime import datetime
from ecl import converter
import entropy.entropy as entropy
import ecl.crypter as crypter
import pathlib

BRAINPOOL160 = "brainpoolP160r1"
BRAINPOOL192 = "brainpoolP192r1"
BRAINPOOL224 = "brainpoolP224r1"
BRAINPOOL256 = "brainpoolP256r1"
BRAINPOOL320 = "brainpoolP320r1"
BRAINPOOL384 = "brainpoolP384r1"
BRAINPOOL512 = "brainpoolP512r1"
extension = ".pem"



def ecl_pvt_key(fileName, index, curve):
    start = datetime.now()
    os.system("openssl ecparam -name " + curve + " -genkey  -out " + fileName)
    end = datetime.now()
    time = end-start
    print(time.total_seconds())
    pub_time = ecl_pub_key(fileName, "./keys/pub_ecl_key" + str(index)+extension)
    return time, pub_time

def ecl_pub_key(privateKey, outputKey):
    start = datetime.now()
    s = os.system("openssl ec -in " + privateKey + " -pubout -out " + outputKey)
    end = datetime.now()
    time = end-start
    print(time.total_seconds())
    return time

def ecl_generate_keys(curve_name,index=0):
    i=0
    tot_pvt = 0
    tot_pub = 0
    pvt_array = []
    pub_array = []

    while i < index:
        res = ecl_pvt_key("./keys/pvt_ecl_key"+str(i)+extension, i, curve_name)
        tot_pvt = tot_pvt + res[0].total_seconds()
        tot_pub = tot_pub + res[1].total_seconds()
        pvt_array.append(res[0].total_seconds())
        pub_array.append(res[1].total_seconds())
        i = i + 1
    avg_pvt= tot_pvt/index
    avg_pub= tot_pub/index
    file = open("./time/time.txt", "w+")
    file.write("TEMPO TOT PRIVATE: "+str(tot_pvt)
               +"\nAVG PVT: " + str(avg_pvt)  +
               "\nTEMPO TOT PUBBLICHE: " +str(tot_pub)+
               "\nAVG PUB: " + str(avg_pub) +
               "\nMAX_PVT: " + str(max(pvt_array)) +
               "\nMIN_PVT: " + str(min(pvt_array)) +
               "\nMAX_PUB: " + str(max(pub_array)) +
               "\nMIN_PUB: " + str(min(pub_array))
               )

def concat_pvt_keys(num):
    i = 0
    s=""
    fout = open('./concatenate_keys/out_concat_pvt.txt',"w+")
    while i < num:
        f = open('./keys/pvt_ecl_key' + str(i) + extension)
        lines = f.readlines()
        s += lines[4].strip() + lines[5].strip() + lines[6].strip()
        f.close()
        i=i+1

    fout.write(s)

def concat_pub_keys(num):
    i = 0
    s=""
    fout = open('./concatenate_keys/out_concat_pbl.txt', "w+")
    while i < num:
        f = open('./keys/pub_ecl_key' + str(i) + extension)
        lines = f.readlines()
        s = s + lines[1].strip() + lines[2].strip()
        s.strip()
        f.close()
        i = i+1

    fout.write(s)

def genSharedKey(index):
    pvt_one = './keys/pvt_ecl_key' + str(index) + '.pem'
    pub_two = './keys/pub_ecl_key' + str(index + 1) + '.pem'
    os.system(
        "openssl pkeyutl -derive -inkey " + pvt_one + " -peerkey " + pub_two + " -out shared_key" + str(index) + ".pem")

def genSharedKeyDec(index):
    pvt_one = './keys/pvt_ecl_key' + str(index+1) + '.pem'
    pub_two = './keys/pub_ecl_key' + str(index) + '.pem'
    os.system(
        "openssl pkeyutl -derive -inkey " + pvt_one + " -peerkey " + pub_two + " -out shared_key" + str(index) + ".pem")

def fileCryprting(index, file):
    tempo = datetime.now()
    genSharedKey(index)
    os.system("openssl enc -aes-256-cbc -k  ./shared_key"+str(index)+".pem"+" -e -in " + file + " -out crypted"+ str(index))
    tempo_end = datetime.now()
    tot = tempo_end - tempo
    f = open("./crypter_files/time_to_encrypt.txt", "w+")
    f.write(str(tot.total_seconds()) + "\n")

def fileDecrypting(index, file):
    tempo = datetime.now()
    genSharedKeyDec(index)
    os.system("openssl enc -aes-256-cbc -k ./shared_key"+str(index)+".pem"+" -d -in " + file + " -out decrypted" + str(index))
    tempo_end = datetime.now()
    tot = tempo_end - tempo
    f = open("./crypter_files/time_to_decrypt.txt", "w+")
    f.write(str(tot.total_seconds()) + "\n")


def crypt_and_decrypt(index, file):
    fileCryprting(index, file)
    fileDecrypting(index, "./crypted1")
    entropy_encrypted_file()


def entropy_encrypted_file():
    entropia = entropy.evaluate_entropy_from_file("./crypted1")



crypt_and_decrypt(1,"../file100.txt")

'''
ecl_generate_keys(BRAINPOOL320,index=100)
concat_pvt_keys(100)
concat_pub_keys(100)
with open('concatenate_keys/out_concat_pvt.txt', 'r') as content_file:
    content = content_file.read().strip()
    converter.from_base64_to_binary(content, "binary_concatenate_keys/binary_concatenate_pvt.txt")

with open('concatenate_keys/out_concat_pbl.txt', 'r') as content_file:
    content = content_file.read().strip()
    converter.from_base64_to_binary(content, "binary_concatenate_keys/binary_concatenate_pbl.txt")
    print("done")

pvt_entropy = entropy.evaluate_entropy_from_file('binary_concatenate_keys/binary_concatenate_pvt.txt')
pbl_entropy = entropy.evaluate_entropy_from_file('binary_concatenate_keys/binary_concatenate_pbl.txt')

open('./entropy/out_concat_pvt_entropy.txt', "w+").write(str(pvt_entropy))
open('./entropy/out_concat_pbl_entropy.txt', "w+").write(str(pbl_entropy))

'''


'''GENERO pvt1 e pub1 e pvt2 e pub2

 openssl pkeyutl -derive -inkey pvt1.pem -peerkey pub2.pem -out SharedSecret1.bin
 openssl pkeyutl -derive -inkey pvt2.pem -peerkey pub1.pem -out SharedSecret2.bin

 enc -aes-256-cbc -k SharedSecret1.bin -e -iter 1000 -salt -in nome_file_decriptato -out nome_file_output
 enc -aes-256-cbc -k SharedSecret1.bin -d -iter 1000 -salt -in nome_file_criptato -out nome_file_decriptato

 openssl pkeyutl -derive -inkey pvt1.bin -peerkey pub2 -out nome_file_chiave_comune
'''