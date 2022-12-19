import random

def xor_cipher():
    message = input("Give me your secrets (Enter - read from file): ")
    key = input("Give me your key (Enter - KeyGeneration): ")

    if not message:
        message = file_reading()
    
    if not key:
        key = "".join(
            random.choice("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
            for i in range(random.randint(1, len(message)))
            )
        print(f"Ok, I do it myself:\n{key}")

    result = bytearray()
    if type(message) == str:
        message = bytearray(message, "utf-8")
    key = bytearray(key, "utf-8")

    for i in range(len(message)):
        result.append(message[i] ^ key[i % len(key)])

    file_writing(result)

def file_writing(data, filename="./text.txt"):
    f = open(filename, "wb")
    f.write(data)
    f.close()

def file_reading(filename="./text.txt"):
    f = open(filename, "rb")
    data = f.read()
    f.close()
    return data

xor_cipher()


