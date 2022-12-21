import random

def xor_cipher():
    """Функция для XOR-шифрования.
    
    Функция совершает XOR-шифрование и расшифровку.  
    Принимает строку (зашифрованную, либо ту которую нужно зашифровать).  
    Возвращает строку (расшифрованную, либо ту которую нужно расшифровать).
    Вызывает функции: file_reading - для чтения из файла, file_writing - для записи в файл.
    
    """
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
    """Функция записи файла.  
   
    Функция принимает строку - data.
    Содержит необязательный аргумент, имя файла под запись - filename.
    Записывает строку data в файл.
   
    """
    f = open(filename, "wb")
    f.write(data)
    f.close()

def file_reading(filename="./text.txt"):
     """Функция чтения файла.  
   
    Содержит необязательный аргумент, имя файла для чтения - filename.
    Возвращает строку data из файла.
   
    """
    f = open(filename, "rb")
    data = f.read()
    f.close()
    return data

xor_cipher()
