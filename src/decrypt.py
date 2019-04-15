from maths import *
from keys import *


class Decrypt:
    def __init__(self, n, d):
        if type(n) != int or type(d) != int:
            raise Exception('Wrong paramaters n and d (all must be integers).')
        self.n = n
        self.d = d

    def text(self, dec_list):
        if type(dec_list) != list:
            return -1

        new_encrypt = []
        for i in dec_list:
            new_encrypt.append((i ** self.d) % self.n)

        return new_encrypt
