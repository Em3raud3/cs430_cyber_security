import time
import codecs
#! Used to time the program

#! Function to encrypt a message
def encrypt(message):
    key = input("Enter the two-lettered key to use to encrypt the message: ")
    start = time.perf_counter()

    key = [ord(key[0]), ord(key[1])] #! Convert the key to ASCII values

    #! Open the file to be encrypted
    with open(message, "r") as file:
        message = file.read()

    #! Loop through each character in the message and perform XOR operation with the key
    #! Store the result in a new string after converting back to Character

    message = "".join(chr(ord(letter) ^ key[index % 2]) for index, letter in enumerate(message))

    print("The encrypted message is: " + message)

    #! Write the encrypted message to a file for testing purposes
    #! Uncomment the line below to write the encrypted message to a file
    # with open("test_encryption.txt", "w") as file:
    #     file.write(message)

    finish = time.perf_counter()
    print(f"\nEncryption took {finish - start} seconds.")


#! function to decrypt a message
def decrypt(message, key):
    start = time.perf_counter()
    key = [ord(key[0]), ord(key[1])] #! Convert the key to ASCII values

    #! Open the file to be encrypted
    with codecs.open(message, encoding="utf8") as file:
        message = file.read()

    #! Loop through each character in the message and perform XOR operation with the key
    #! Store the result in a new string after converting back to Character
    message = ''.join(chr(ord(letter) ^ key[index % 2]) for index, letter in enumerate(message))

    print("The decrypted message is: " + message)

    #! Write the encrypted message to a file for texting purposes
    #! Uncomment the line below to write the encrypted message to a file
    # with open("test_decryption.txt", "w") as file:
    #     file.write(message)

    finish = time.perf_counter()
    print(f"\nDecryption took {finish - start} seconds.")

    print("The decrypted message is: " + message)

    finish = time.perf_counter()
    print(f"\nDecryption took {finish - start} seconds.")


#! function to brute force a message
def brute_force(message, dictionary):
    start = time.perf_counter()

    finish = time.perf_counter()
    print(f"\nBrute force took {finish - start} seconds.")


def main():

    print("This program will encrypt and decrypt messages.")
    #! Store Dictionary in a Set because it has O(1) lookup time
    #! Length of the dictionary is 80368
    with open("Dictionary.txt", "r") as allwords:
        dictionary = set(allwords.read().splitlines())

        #! Ask user for what operation to perform
        print("Would you like to encrypt(1), decrypt(2), or brute force(3) a message? ")
        prompt = input("Enter 1, 2, or 3: ")

        while prompt != "1" and prompt != "2" and prompt != "3":
            print("Please enter a valid number.\n")
            prompt = input("Enter 1, 2, or 3: ")
            print(prompt)

        if prompt == "1":
            print("You have chosen to encrypt a message.")
            file = input("Enter the name of the file you would like to encrypt: ")
            encrypt(file)

        elif prompt == "2":
            print("You have chosen to decrypt a message.")
            file = input("Enter the name of the file you would like to decrypt: ")
            key = input("Enter the two-lettered key to use to decrypt the message: ")
            decrypt(file, key)

        else:
            print("You have chosen to brute force a message.")
            file = input("Enter the name of the file you would like to brute force: ")
            brute_force(file, dictionary)

if __name__ == "__main__":
    main()