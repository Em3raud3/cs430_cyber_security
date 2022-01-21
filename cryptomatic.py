# Author: Jeffrey Weng
# Compiler: Python 3.8.10

# Useage: 1: Place "crytopmatic.py", "Dictionary.txt" in the same directory.
#         2: run cryptomatic.py
#         3: Message from brute force will automatically be written to "Brute_Force_Message.txt"

import codecs
import itertools
import time
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

    print("The encrypted message is:\n" + message)

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

    print("The decrypted message is:\n\n" + message)

    finish = time.perf_counter()
    print(f"\nDecryption took {finish - start} seconds.")

    print("The decrypted message is: " + message)

    finish = time.perf_counter()
    print(f"\nDecryption took {finish - start} seconds.")


#! function to brute force a message
def brute_force(message):
    #! Store Dictionary in a Set because it has O(1) lookup time
    with open("Dictionary.txt", "r") as allwords:
        dictionary = set(allwords.read().splitlines())

        start = time.perf_counter()

        #! Create a list of the range of all the ascii value of all valid characters
        ascii_array = [i for i in range(32, 127)]

        with codecs.open(message, encoding="utf8") as file:
            message = file.read()

            #! Loop through each possible combination of two letters and stores in list
            for index, key in enumerate(itertools.product(ascii_array, repeat=2)):

                #! Decrypt the message with the current key
                test_message = "".join(chr(ord(letter) ^ key[index % 2]) for index, letter in enumerate(message)).split()
                word_count = len(test_message)
                matches = 0

                #! Check if the word is in the dictionary and keep count of matches.
                for index in range(0, word_count):
                    if test_message[index].lower() in dictionary: #! Words in dictionary are all lowercase, so convert to lowercase
                        matches += 1
                    else:
                        matches -= 1

                if matches > 0: #! If matches is positive, print the key and write message to file
                    print(f"\nThe Key is: {chr(key[0]) + chr(key[1])}\n")
                    message = "".join(chr(ord(letter) ^ key[index % 2]) for index, letter in enumerate(message))

                    #! Write the message to a file
                    with open("Brute_Force_Message.txt", "w") as file:
                        file.write(message)

                    print("The message has been written to Brute_Force_Message.txt\n")

                    finish = time.perf_counter()
                    print(f"Brute force took: {finish - start} seconds to complete.")
                    break

            #! If no matches are found, print that no matches were found
            else:
                print("No keys found.")

def main():

    print("This program will encrypt and decrypt messages.")

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
        brute_force(file)

if __name__ == "__main__":
    main()