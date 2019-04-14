from Cryptography import *
import csv
import random


def main():
    go = int(input("\nYou want:\n\t0: Encrypt\n\t1: Decrypt\n\tYour answer: "))

    if go == 0:
        txt = input("\nEnter the text: ")
        print("\nEnter with two number primers (p and q): ")
        p = int(input("\tP: "))
        q = int(input("\tQ: "))
        encrypt = Encrypt(p, q)
        print('Encrypting...')
        csv_out = encrypt.text(txt)

        with open(file='encrypt.csv', mode='w') as file:
            for i in csv_out:
                file.write(str(i) + '\n')

        print(f"\nYour keys:\n\tn: {encrypt.n}\n\td; {encrypt.d}\n\nIt's finished")

    elif go == 1:
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
        print("Enter a valid option!")
        return -1

    return 1


if __name__ == '__main__':
    main()
