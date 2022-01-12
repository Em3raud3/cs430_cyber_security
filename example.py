
# Python program to show
# bitwise operators

message = ord("H")
# message = format(message, '08b')


key = ord("a")
# key = format(key, '08b')

print(message)
print(key)

encrypt = message ^ key
print(encrypt)
print(format(encrypt, '08b'))

# print bitwise XOR operation






# 01001000
# 01100001
# 00101001