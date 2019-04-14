from MatFunctions import MatFunctions
from Keys import Keys


class Encrypt:
    def __init__(self, p, q):
        self.n = p * q
        self.phi = MatFunctions.phi(p, q)
        self.e = Keys.public(self.phi, self.n)
        self.d = Keys.private(self.e, self.phi)

    def text(self, string):
        if type(string) != str:
            return -1

        chars = list(string)
        new_encrypt = []
        for i in chars:
            new_encrypt.append((ord(i) ** self.e) % self.n)

        return new_encrypt


class Decrypt:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def text(self, dec_list):
        if type(dec_list) != list:
            return -1

        print(f'n: {self.n}')
        new_encrypt = []
        for i in dec_list:
            new_encrypt.append((i ** self.d) % self.n)

        return new_encrypt
