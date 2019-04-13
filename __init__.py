from Cryptography import Cryptography


def main():
    go = int(input("\nYou want:\n\t0:Encrypt\n\t1: Decrypt\n\tYour answer: "))

    if go == 0:
        work = int(input("\nYou want to work with:\n\t0: Files\n\t1:Text\n\tYour answer: "))

        if work == 0:
            file = input("\nWhich file do you want to encrypt?\t(Remember for a extension)\n")
        elif work == 1:
            text = input("\nEnter the text: ")
        else:
            print("\nEnter a valid option!")

            return -1

        print("\nEnter with two number primers (p and q): ")
        p = int(input("     P: "))
        q = int(input("     Q: "))

        crypto = Cryptography(p, q, 100, 200)

        if work == 0:
            pass
        elif work == 1:
            crypto.Encrypt.text(text)

    elif go == 1:
        file = input("Which file do you want to decrypt?\t (Remember for a extension it's (.enc)\n")
    else:
        print("Enter a valid option!")

        return -1

    return 1


if __name__ == '__main__':
    main()
