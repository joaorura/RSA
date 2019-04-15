from encrypt import *
from decrypt import *
from keys import *
from man import *
import csv
import random
import sys

def main(argv):
    if "generate" in argv:
        print("Please provide two prime numbers, P and Q:")
        p = int(input("\tp: "))
        q = int(input("\tq: "))

        if Math.is_prime(p) == False or Math.is_prime(q) == False:
            print("One of them is not a prime number!")
            return

        keys = Generate_keys(p, q)
        print("\nYour keys:")
        print("\tPublic key (n, e):", keys.public.n,",", keys.public.e)
        print("\tPrivate key (p, q, d):", p, ",", q, ",", keys.private.d)

    elif "encrypt" in argv:
        print("Please provide the name of the file you wish to encrypt and your public key:")

        file_name = input("\tFile name: ")

        print("\tPublic key (n, e):")
        n = int(input("\t\tn: "))
        e = int(input("\t\te: "))

        with open(file_name, "r") as file:
            text = file.read()

        print('\nEncrypting...')
        csv_out = Encrypt.text(Encrypt, text, n, e)

        file_name = input("\nName the csv file: ")

        with open(file=file_name, mode='w') as file:
            for i in csv_out:
                file.write(str(i) + '\n')

    elif "decrypt" in argv:
        print("Please provide the name of the file you wish to decrypt and your private key:")

        file_name = input("\tFile name: ")

        print("\tPrivate key (p, q, d):")
        p = int(input("\t\tp: "))
        q = int(input("\t\tq: "))
        n = p * q
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
