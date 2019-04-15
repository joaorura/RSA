from cryptography import *
import csv
import random
import sys
from man import *

def main(args=None,primes=None,files=None):
    if args is None and primes is None and files is None:
        args = sys.argv[1:2]
        primes = sys.argv[2:4]
        int_primes = [int(n) for n in primes]
        files = ''.join(sys.argv[4:5])

    if "encrypt" in args:

        p = int(int_primes[0])
        q = int(int_primes[1])
        
        with open(str(files), "r") as file:
            text = file.read().splitlines()

        encrypt = Encrypt(p, q)
        print('Encrypting...')
        csv_out = encrypt.text(str(files))
        
        with open(file='encrypt.csv', mode='w') as file:
            for i in csv_out:
                file.write(str(i) + '\n')

        print(f"\nYour keys:\n\tn: {encrypt.n}\n\td; {encrypt.d}\n\nIt's finished")

    elif "decrypt" in args:
        file_name = input("\nWhich file do you want to decrypt?\t " +
                          "(Remember for a extension it's (.csv)\n\tYour answer: ")
        print("\nEnter with the keys (n and d): ")
        with open(file=file_name, mode='r') as file:
            read = []
            for row in csv.reader(file):
                read.append(int(row[0]))

        n = int(input("\tn: "))
        d = int(input("\td: "))

        print("Decrypting...")
        decrypt = Decrypt(n, d)
        print(decrypt.text(read))
        string_decry = ''.join(chr(i) for i in decrypt.text(read))

        print(f"Your text: {string_decry}\nIt's finished\n")
    else:
        usage()
        sys.exit(1)
main()
