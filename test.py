# st = "hello world"
# ' '.join(format(ord(x), 'b') for x in st)
# '1101000 1100101 1101100 1101100 1101111 100000 1110111 1101111 1110010 1101100 1100100'
import codecs
#! 100000 mean a empty space

key = "xl"
key = [ord(key[0]), ord(key[1])] #! Convert the key to ASCII values

with codecs.open("encrypted-xl.txt", encoding="utf8") as file:
    message = file.read()

    # print(message) #! Print the message to be encrypted

    # for i in message:
    #     print(ord(i)) #* This does print out the right binary values

    #! Convert the message to Binary
    message = "".join(chr(ord(letter) ^ key[index % 2]) for index,letter in enumerate(message))
    print(message)

    # for i in message:
    #     print(i)








#! u 01110101
#! x 01111000
#!   00001101

#! r 01110110
#! l 01101100
#!   00011010

# 00111110
# 00000011
# 00001010
# 00011110