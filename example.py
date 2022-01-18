
message = ""
key = "xl"
key = [ord(key[0]), ord(key[1])] #! Convert the key to ASCII values

#! Open the file to be encrypted
with open("Lincoln.txt", "r") as file:
    message = file.read()

print(message)

# speech = ""

# for i, j in enumerate(message):
#     speech += format(ord(j) ^ key[i % 2], '08b')

# character_split = [speech[y-8:y] for y in range(8, len(speech)+8, 8)]

# speech = int(speech, 2)
# speech = speech.to_bytes((speech.bit_length() + 7) // 8, 'big').decode()

# print(speech)
# Python program to show
# bitwise operators

# message = ord("u")
# # # message = format(message, '08b')
# print(format(message, '08b'))

# key = ord("x")
# print(format(key, '08b'))

# # print(message)
# # print(key)

# encrypt = message ^ key
# # print(encrypt)

# print(format(encrypt, '08b'))

# print("\ndecrypting")

# print bitwise XOR operation

# 01110101
# 01111000
# 00001101