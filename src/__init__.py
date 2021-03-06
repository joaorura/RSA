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
        print("Please provide two prime numbers, p, q and e:")
        p = int(input("\tp: "))
        q = int(input("\tq: "))
        e = int(input("\te: "))

        if Math.is_prime(p) == False:
            print("\np is not a prime number!")
            return

        if Math.is_prime(q) == False:
            print("\nq is not a prime number!")
            return

        print("\nPlease provide the name of the file you wish write your keys:")
        file_name = input("\tFile name: ")

        keys = GenerateKeys(p, q, e)

        if keys.public.n < 26:
            print("q and p it's small")
            return

        with open(file_name, "w") as file:
            file.write("Your keys:\n")
            file.write(f"\tPublic key: (n, e): {keys.public.n}, {keys.public.e}\n")
            file.write(f"\tPrivate key: (p, q, d): {p}, {q}, {keys.private.d}\n")

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
            d = int(input("\t\td: "))
            n = p * q

        decry = Decrypt(n, d)
        print("\nDecrypting...")
        if 'file' in argv:
            decry.file(file_name)
        else:
            with open(file=file_name, mode='r') as file:
                read = []
                for row in csv.reader(file):
                    read.append(int(row[0]))

            string = ''
            for i in decry.text(read):
                if i == 26:
                    a = 32
                    a = a.to_bytes(1, byteorder='big', signed=False)
                else:
                    a = i + 65
                    a = a.to_bytes(1, byteorder='big', signed=False)
                    
                string += a.decode('ASCII')

            file_name = input("\nName the decrypted file: ")
            with open(file=file_name, mode="w") as file:
                file.write(string)
    else:
        usage()
        sys.exit(1)

    print("\nIt's finished!")


if __name__ == "__main__":
    main(sys.argv)
