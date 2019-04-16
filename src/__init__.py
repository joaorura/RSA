import csv
import sys

from decrypt import *
from encrypt import *
from keys import *
from man import *
from maths import *
from clr_file import *

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
        print(f"\tPrivate key: (p, q, d): {p}, {q}, {keys.private.d}")

    elif "encrypt" in argv:
        print("Please provide the name of the file you wish to encrypt and your public key:")

        file_name = input("\tFile name: ")

        if 'file' in argv:
            n = 6533
            e = 5
        else:
            print("\tPublic key (n, e):")
            n = int(input("\t\tn: "))
            e = int(input("\t\te: "))

        print('\nEncrypting...')
        encrypt = Encrypt(n, e)

        if 'file' in argv:
            encrypt.file(file_name)
        else:
            with open(file_name, "r") as file:
               text = file.read()

            csv_out = encrypt.text(text)
            file_name = input("\nName the csv file: ")
            with open(file=file_name, mode='w') as file:
                for i in csv_out:
                    file.write(str(i) + '\n')

    elif "decrypt" in argv:
        print("Please provide the name of the file you wish to decrypt and your private key:")

        file_name = input("\tFile name: ")

        if 'file' in argv:
            n = 6533
            d = 83
        else:
            print("\tPrivate key: (p, q, d):")
            p = int(input("\t\tp: "))
            q = int(input("\t\tq: "))
            n = p * q
            d = int(input("\t\td: "))

        decry = Decrypt(n, d)
        print("\nDecrypting...")
        if 'file' in argv:
            decry.file(file_name)
        else:
            with open(file=file_name, mode='r') as file:
                read = []
                for row in csv.reader(file):
                    read.append(int(row[0]))

            string = ''.join(chr(i) for i in decry.text(read))
            file_name = input("\nName the decrypted file: ")
            with open(file=file_name, mode="w") as file:
                file.write(string)
    else:
        usage()
        sys.exit(1)

    print("\nIt's finished!")


if __name__ == "__main__":
    main(sys.argv)
