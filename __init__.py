from Cryptography import Encrypt
from Cryptography import Decrypt
import csv


def main():
    go = int(input("\nYou want:\n\t0:Encrypt\n\t1: Decrypt\n\tYour answer: "))

    if go == 0:
        txt = input("\nEnter the text: ")
        print("\nEnter with two number primers (p and q): ")
        p = int(input("\tP: "))
        q = int(input("\tQ: "))
        encrypt = Encrypt(p, q, 100, 200)
        csv_out = encrypt.text(txt)

        with open(file='encrypt.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writecolumns(str(i) for i in csv_out)
    elif go == 1:
        file_name = input("Which file do you want to decrypt?\t (Remember for a extension it's (.csv)\n\tYour answer: ")
        print("\nEnter with the keys (n and d): ")

        with open(file=file_name, mode='r') as file:
            read = csv.reader(file)

        n = int(input("\tn: "))
        e = int(input("\te: "))
        decrypt = Decrypt(n, e)
        string_decry = ''.join(str(i) for i in decrypt.text(read))

        print(f"Your text: {string_decry}")
    else:
        print("Enter a valid option!")
        return -1

    return 1


if __name__ == '__main__':
    main()
