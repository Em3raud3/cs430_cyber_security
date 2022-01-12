import time
#! Used to time the program

#! Function to encrypt a message
def encrypt(message, key):
    start = time.perf_counter()



    finish = time.perf_counter()
    print(f"\nEncryption took {finish - start} seconds.")


#! function to decrypt a message
def decrypt(message, key, dictionary):
    start = time.perf_counter()

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
            encrypt(file, dictionary)

        elif prompt == "2":
            print("You have chosen to decrypt a message.")
            file = input("Enter the name of the file you would like to decrypt: ")
            key = input("Enter the two-lettered key to use to decrypt the message: ")
            decrypt(file, key, dictionary)

        else:
            print("You have chosen to brute force a message.")
            file = input("Enter the name of the file you would like to brute force: ")
            brute_force(file, dictionary)

    # message = "Hello World"5
    # key = "ab"

    # for i in message:
    #     print(f"{ord(i)} {i}")

    # print("\nkey is \n")
    # for i in key:
    #     print(f"{ord(i)} {i}")

if __name__ == "__main__":
    main()