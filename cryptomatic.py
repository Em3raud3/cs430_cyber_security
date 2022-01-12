
def encrypt(message, key):
    pass

def decrypt(message, key, dictionary):
    pass

def brute_force(message, key, dictionary):
    pass

def main():

    print("This program will encrypt and decrypt messages.")
    #! Store Dictionary in a Set because it has O(1) lookup time
    with open("Dictionary.txt", "r") as allwords:
        dictionary = allwords.read().splitlines()

        #! Ask user for what operation to perform
        print("Would you like to encrypt(1), decrypt(2), or brute force(3) a message? ")
        prompt = input("Enter 1, 2, or 3: ")

        while prompt != "1" and prompt != "2" and prompt != "3":
            print("Please enter a valid number.\n")
            prompt = input("Enter 1, 2, or 3: ")
            print(prompt)

        if prompt == "1":
            print("You have chosen to encrypt a message.")
            encrypt(dictionary)

        elif prompt == "2":
            print("You have chosen to decrypt a message.")
            decrypt(dictionary)

        else:
            print("You have chosen to brute force a message.")
            brute_force(dictionary)

    # message = "Hello World"5
    # key = "ab"

    # for i in message:
    #     print(f"{ord(i)} {i}")

    # print("\nkey is \n")
    # for i in key:
    #     print(f"{ord(i)} {i}")

if __name__ == "__main__":
    main()