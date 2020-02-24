import math


def shannon(data,filename,case):
    '''
    Performs a Shannon entropy analysis on a given block of data.
    '''
    entropy = 0
    if data:
        length = len(data)

        seen = dict(((chr(x), 0) for x in range(0, 256)))
        for byte in data:
            seen[byte] += 1

        for x in range(0, 256):
            p_x = float(seen[chr(x)]) / length
            if p_x > 0:
                entropy -= p_x * math.log(p_x, 2)
    print("entropy: " + str(entropy/8))
    if case == "OS":
        f = open("concatenate_keys/entropy_concatenate_keys_OS.txt", "w")
        f.write(str(entropy / 8))
    if case == "PYTHON":
        f = open("concatenate_keys/entropy_concatenate_keys_python.txt", "w")
        f.write(str(entropy / 8))
    if case == "BUTTERFLY":
        f = open("concatenate_keys/entropy_concatenate_keys_butterfly.txt", "w")
        f.write(str(entropy / 8))
    if case == "UNI":
        f = open("concatenate_keys/entropy_concatenate_keys_uniform.txt", "w")
        f.write(str(entropy / 8))

    f.close()

    return (entropy / 8)


def evaluate_entropy_from_file(filename, case):
    f = open(filename, 'rb')
    li = []
    while (True):
        x = f.read(1)
        if x == b'':
            break
        li.append(chr(int.from_bytes(x, byteorder='big')))

    return shannon(li, filename,case)