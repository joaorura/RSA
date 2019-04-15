from encrypt import *
from decrypt import *
from keys import *
from maths import *
from man import *
import csv
import sys


def main(argv):
    if "generate" in argv:
        print("Please provide two prime numbers, P and Q:")
        p = int(input("\tp: "))
        q = int(input("\tq: "))

        if Math.is_prime(p) == False or Math.is_prime(q) == False:
            print("One of them is not a prime number!")
            return

        keys = GenerateKeys(p, q)
        print("\nYour keys:")
        print(f"\tPublic key: (n, e): {keys.public.n}, {keys.public.e}")
        print(f"\tPrivate key: (n, d): {keys.public.n}, {keys.private.d}")

    elif "encrypt" in argv:
        print("Please provide the name of the file you wish to encrypt and your public key:")

        file_name = input("\tFile name: ")

        print("\tPublic key (n, e):")
        n = int(input("\t\tn: "))
        e = int(input("\t\te: "))

        with open(file_name, "r") as file:
            text = file.read()

        print('\nEncrypting...')
        encrypt = Encrypt(n, e)
        csv_out = encrypt.text(text)

        file_name = input("\nName the csv file: ")

        with open(file=file_name, mode='w') as file:
            for i in csv_out:
                file.write(str(i) + '\n')

    elif "decrypt" in argv:
        print("Please provide the name of the file you wish to decrypt and your private key:")

        file_name = input("\tFile name: ")
        # file_name = '/home/joaorura/my_workspace/RSA/src/encyrpt.csv'

        print("\tPrivate key: (n, d):")
        n = int(input("\t\tn: "))
        d = int(input("\t\td: "))

        with open(file=file_name, mode='r') as file:
            read = []
            for row in csv.reader(file):
                read.append(int(row[0]))

        print("\nDecrypting...")
        decrypt = Decrypt(n, d)
        string = ''.join(chr(i) for i in decrypt.text(read))

        file_name = input("\nName the decrypted file: ")

        with open(file=file_name, mode="w") as file:
            file.write(string)
    else:
        usage()
        sys.exit(1)

    print("\nIt's finished!")


if __name__ == "__main__":
    main(sys.argv)
