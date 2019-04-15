from maths import *
from keys import *

class Decrypt:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def text(self, dec_list):
        if type(dec_list) != list:
            return -1

        new_encrypt = []
        for i in dec_list:
            new_encrypt.append((i ** self.d) % self.n)

        return new_encrypt
