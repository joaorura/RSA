from encrypt import *
from decrypt import *
from keys import *
from man import *
import csv
import random
import sys

def main(args=None,primes=None,files=None):
    if args is None and primes is None and files is None:
        args = sys.argv[1:2]
        primes = sys.argv[2:4]
        int_primes = [n for n in primes]
        files = ''.join(sys.argv[4:5])

    if "encrypt" in args:

        p = int(int_primes[0])
        q = int(int_primes[1])

        if Math.is_prime(p) == False or Math.is_prime(q) == False:
            print("One of them is not a prime number!")
            return

        keys = Generate_keys(p, q)

        with open(files, "r") as file:
            text = file.read()

        print('Encrypting...')
        csv_out = Encrypt.text(Encrypt, text, keys.public.e, keys.public.n)

        with open(file='encrypt.csv', mode='w') as file:
            for i in csv_out:
                file.write(str(i) + '\n')

        print("\nYour keys:\n\tn:", keys.public.n, "\n\td:", keys.private.d, "\n\nIt's finished")

    elif "decrypt" in args:
        with open(file=primes[0], mode='r') as file:
            read = []
            for row in csv.reader(file):
                read.append(int(row[0]))

        n = int(input("\tn: "))
        d = int(input("\td: "))

        print("Decrypting...")
        decrypt = Decrypt(n, d)
        string_decry = ''.join(chr(i) for i in decrypt.text(read))

        print(f"Your text: {string_decry}\nIt's finished\n")
    else:
        usage()
        sys.exit(1)

if __name__ == "__main__":
    main()
