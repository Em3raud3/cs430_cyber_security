
key = "x"
key = "xl"
key = [ord(key[0]), ord(key[1])] #! Convert the key to ASCII values

with open("short.txt", encoding='utf8', errors='ignore') as file:
    message = file.read()
    
    print(message)
    
    message = "".join(chr(ord(letter) ^ key[index % 2]) for index,letter in enumerate(message))
    
    print(message)
    
    message = "".join(chr(ord(letter) ^ key[index % 2]) for index,letter in enumerate(message))
    print(message)