from itertools import cycle

string = open("FFVII").read()

def repeated_xor(string,key):
    result=" "
    for c, k in zip(string,cycle(key)):
       result += chr(ord(c) ^ ord(k))
    return result

print(repeated_xor(string,"cloud"))
