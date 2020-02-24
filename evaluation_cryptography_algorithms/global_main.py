import entropy.entropy_2 as en
import aes.crypter as aesc
import ecl,blowfish2,rsa_p

nome_file_random="Butterfly_files/file100.txt"

#File da 3 mb con butterfly
print("entropu: " ,en.evaluate_entropy_from_file_random(nome_file_random))
aesc.encrypt_file(nome_file_random,)

