import entropy.entropy as entropy
import entropy.entropy_2 as entropy2
import rsa_p.rsa_generator as rsa_generator
import rsa_p.converter as converter
import rsa_p.crypter as crypter

''''''
numero_bit_key= '2048'
file_privKey='./keys/key'
file_pubKey='./keys/pubkey'


'''
#GENERA COPPIE DI CHIAVI 
rsa_generator.generate_all(file_privKey, file_pubKey, 400, 2048)
'''

''''''

#CALCOLA ENTROPIA SULLA CONCATENAZIONE DELLE CHIAVI
converter.binary_contatenate_keys()
entropy.evaluate_entropy_from_file("binary_concatenate_keys/binary_concatenate_pvt.txt")
entropy.evaluate_entropy_from_file("binary_concatenate_keys/binary_concatenate_pbl.txt")



'''
#CALCOLO ENTROPIA SU FILE DI 245BYTE GIA CRIPTATO CON RSA 
entropy2.evaluate_entropy_from_file_crypted("crypted_245byte.txt")
'''

'''
#CALCOLO ENTROPIA SU UN FILE DI 3 MEGA
entropy2.evaluate_entropy_from_file_crypted("crypted_file3.txt")
'''


'''
PER CRIPTARE E DECRIPTARE VAI SU CRYPTER.PY
'''


















