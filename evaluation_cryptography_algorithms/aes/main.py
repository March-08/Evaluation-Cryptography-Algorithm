
import aes.crypter as cry
import random
import entropy.entropy_2 as entropy
import  aes.aes_generator as gen

N=10
index=random.randint(0,N-1)
case="OS"



'''
#GENERAZIONE CHIAVI AES
gen.generate_n_keys(12,case)
'''


'''
#CRIPTA E DECRIPTA: sceglie una file con una chiave estrae key e iv le usa per la de/criptazione

f=open("keys/key"+str(index)+".pem")
key=str(f.readline()[4:-1])
iv=str(f.readline()[4:-1])

cry.encrypt_file("../Butterfly_files/file100.txt", key,0)
cry.decrypt_file("crypter_files_time/encrypted.txt", key,0)

'''


'''
#CALCOLO ENTROPIA 
entropy.evaluate_entropy_from_file_crypted("crypter_files_time/encrypted.txt")
'''

