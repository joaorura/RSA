import MatFunctions
import Keys


class Cryptography:
    def __init__(self, p, q, a, b):
        self.n = p * q
        self.phi = MatFunctions.phi(p, q)
        self.e = Keys.public(self.phi, self.n)
        self.d = Keys.private(self.e, self.phi, a, b)


class Encrypt(Cryptography):
    def text(self, string):
        if type(string) != "<class 'str'>":
            return -1

        chars = list(string)
        new_encrypt = []
        j = 0
        for i in chars:
            new_encrypt[j] = int(i) ** self.e
            new_encrypt[j] %= self.n
            j += 1

        return new_encrypt


class Decrypt(Cryptography):
    def text(self, string):
        if type(string) != "<class 'str'>":
            return -1

        chars = list(string)
        new_encrypt = []
        j = 0
        for i in chars:
            new_encrypt[j] = int(i) ** self.d
            new_encrypt[j] %= self.n
            j += 1

        return new_encrypt
