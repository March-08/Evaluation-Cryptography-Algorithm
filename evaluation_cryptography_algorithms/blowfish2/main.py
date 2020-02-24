import blowfish2.blowfish_generator as gen
import blowfish2.crypter as cry
import random
import entropy.entropy_2 as entropy
import blowfish2.converter as converter
import os


N = 100

index=random.randint(0,N-1)
case="PYTHON"

print("ecoooo")

gen.generate_n_keys(N, case)
converter.binary_contatenate_keys()
f = open("keys/key"+str(index)+".pem")
f.readline()
key = str(f.readline()[4:-1])
print("KEYYYYYYYYYYYYYYYYY",key)
iv = str(f.readline()[4:-1])
f.close()

print(index)

print("KEY", key)
cry.encrypt_file("../file100.txt", key, iv)
cry.decrypt_file("crypter_files/encrypted.txt", key, iv)
a = 0
a = entropy.evaluate_entropy_from_file_crypted("crypter_files/encrypted.txt")
print(a)

