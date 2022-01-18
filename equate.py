message1 = ""
message2 = ""

with open("test_encryption.txt", "r") as file:
    secret = file.read()
    message1 = secret

with open("encrypted-xl.txt", "r") as file:
    secret2 = file.read()
    message2 = secret2

same = 0
diff = 0
for i,j in zip(message1, message2):
    if ord(i) == ord(j):
        same += 1
    else:
        diff += 1

print("same: " + str(same))
print("diff: " + str(diff))
