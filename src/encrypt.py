from maths import *
from keys import *

class Encrypt:
    def text(self, string, e, n):
        if type(string) != str:
            return -1

        chars = list(string)
        new_encrypt = []
        for i in chars:
            new_encrypt.append((ord(i) ** e) % n)

        return new_encrypt
