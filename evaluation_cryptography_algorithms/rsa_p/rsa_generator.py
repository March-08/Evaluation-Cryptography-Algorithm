import os
from datetime import datetime

numero_bit_key= '2048'
file_privKey='./keys/key'
file_pubKey='./keys/pubkey'
extension_pem=".pem"
extension_der=".der"

#file_to_cript =  'text.txt'
#cripted_file='text_cript.txt'
#decrypted_file='text_decripted.txt'



def rsa_pvt_key(file_privKey, num_bit_key):
    start =datetime.now()
    os.system('openssl genrsa -out ' + file_privKey + ' ' +  str(num_bit_key))
    end = datetime.now()
    time_taken_to_generate_key = end - start
    print('Tempo generazione chiave: ', time_taken_to_generate_key.total_seconds())
    return time_taken_to_generate_key.total_seconds()




def rsa_pbl_key(file_privKey,file_pubKey):
    start = datetime.now()
    os.system('openssl rsa -in ' + file_privKey + ' -pubout' + file_pubKey)
    end = datetime.now()
    time_taken_to_generate_key = end - start
    print('Tempo generazione chiave: ', time_taken_to_generate_key.total_seconds())
    return time_taken_to_generate_key.total_seconds()


def rsa_key_pair(file_privKey,file_pubKey,num_bit_key):
    time1=rsa_pvt_key(file_privKey,num_bit_key)
    time2= rsa_pbl_key(file_privKey,file_pubKey)
    return time1,time2




def generate_n_pairs_keys(file_privKey, file_pblKey, n, num_bit):
    total_pvt_seconds=0
    total_pbl_seconds=0

    time_pvt_keys = []
    time_pbl_keys = []


    for i in range(n):
        time_pvt = rsa_pvt_key(file_privKey+str(i)+extension_der, num_bit)
        time_pbl = rsa_pbl_key(file_privKey+str(i)+ extension_der, file_pblKey+str(i)+ extension_der)

        time_pvt_keys.append(time_pvt)
        time_pbl_keys.append(time_pbl)


        total_pvt_seconds += time_pvt
        total_pbl_seconds += time_pbl

    print("time 1 : " + str(total_pvt_seconds) + " time 2 : " + str(total_pbl_seconds))
    fout =open("./time/timeKeys.txt", "w+")
    fout.write("avg private keys : " + str(total_pvt_seconds/n) + "\navg public keys : " + str(total_pbl_seconds/n))

    fout.write("\nmax_pvt_key: "+str(max(time_pvt_keys)))
    fout.write("\nmax_pbl_key: "+str(max(time_pbl_keys)))

    fout.write("\nmin_pvt_key: "+str(max(time_pvt_keys)))
    fout.write("\nmin_pbl_key: "+str(max(time_pbl_keys)))

    fout.write("\ntotal_private_keys : " + str(total_pvt_seconds) + "\ntotal_public_keys : " + str(total_pbl_seconds))





    fout.close()


    return total_pvt_seconds/n, total_pbl_seconds/n


def get_string_from_pvt_key(file_privKey):
    s=""
    f=open(file_privKey)
    lines=f.readlines()
    lines=lines[1:-1]
    s=""
    for line in lines:
        s+=line.strip()
    print(s)

    return s


def get_string_from_pbl_key(file_publKey):
    s=""
    f=open(file_publKey)
    lines=f.readlines()
    lines=lines[1:-1]
    s=""
    for line in lines:
        s+=line.strip()
    print(s)
    return s



def get_n_strings_from_pvt_keys(file_privKey,n):
    s=""
    for i in range (n):
        out=get_string_from_pvt_key(file_privKey+str(i)+ extension_der)
        s+=out
    f=open("./concatenate_keys/out_concat_pvt.txt","w+")
    f.write(s)
    f.close()
    print(s)
    return s


def get_n_strings_from_pbl_keys(file_pblKeys,n):
    s=""
    for i in range (n):
        out=get_string_from_pbl_key(file_pblKeys+str(i)+ extension_der)
        s+=out
    f=open("./concatenate_keys/out_concat_pbl.txt","w+")
    f.write(s)
    f.close()
    print(s)
    return s


def generate_all(file_pvt, file_pbl, n, num_bit):
    generate_n_pairs_keys(file_pvt, file_pbl, n, num_bit)
    get_n_strings_from_pvt_keys(file_pvt, n)
    get_n_strings_from_pbl_keys(file_pbl, n)



#generate_all(file_privKey,file_pubKey,10,512)

