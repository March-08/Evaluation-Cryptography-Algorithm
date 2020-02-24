import os
from datetime import datetime
import random
import subprocess
import base64

def generate_key(random_string,index):
    start = datetime.now()
    #os.system("openssl enc -aes-256-cbc  -salt  -pbkdf2 -k " + random_string + "  -P > keys/key"+str(index)+".pem")
    print(random_string)
    os.system("openssl enc -bf -salt  -k " + str(random_string) + " -base64 -P  > keys/key" + str(index) + ".pem")
    end = datetime.now()
    time_taken_to_generate_key = end - start
    print('Tempo generazione chiave: ', time_taken_to_generate_key.total_seconds())
    return time_taken_to_generate_key.total_seconds()

def generate_n_keys(n,case):
    time_tot=0
    array_temp = generate_random_array(n, case)
    for index in range(len(array_temp)):
        time_tot += generate_key(array_temp[index], index)
    array_temp = None
    print(str(n)+" chiavi generate")
    f = open("time/avgTimeKeys.txt", "w+")
    f.write(str(time_tot/n))
    f.close()
    concatenate_keys(n)


#usa generatore random di openssl per creare array di stringhe random
def generate_random_array(n, case):
    random_array = []
    output = ""
    for index in range(n):
        if case == "OS":
            #output = subprocess.check_output("openssl rand -base64 128", shell=True)
            #output = output.decode("utf-8").strip()

            output=subprocess.check_output("openssl rand -hex 64", shell=True)

        if case == "PYTHON":
            output = random.getrandbits(1024)
        if case == "BUTTERFLY":
            output = "butterfly"
        if case == "UNI":
            output = "11"

        random_array.append(output)


    return random_array


def get_string_from_key(file_privKey):
    f=open(file_privKey)
    lines=f.readlines()
    line = lines[1]
    line=line[4:-1]
    print(line)
    return line

def concatenate_keys(n):
    concate=""
    for i in range(n):
        concate += str(get_string_from_key("./keys/key"+str(i)+".pem"))
    f = open("concatenate_keys/concatenate_keys.pem", "w+")
    f.write(concate)
    f.close()
    print(concate)
    return concate


#generate_n_keys(["ciao","ciao"],2)
#generate_random_string()

if __name__ == '__main__':
    generate_n_keys(1000)

#generate_random_array(3)
    get_string_from_key("keys/key0.pem")

