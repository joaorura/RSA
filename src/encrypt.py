from maths import *
from keys import *
import sys


class Encrypt:
    def __init__(self, n, e):
        if type(n) != int or type(e) != int:
            raise Exception('Wrong paramater (all must be integers).')

        self.n = n
        self.e = e

    def text(self, string):
        if type(string) != str:
            raise Exception('Wrong paramater must be str, but you send a {type(string)}.')

        chars = list(string)
        new_encrypt = []
        for i in chars:
            new_encrypt.append((ord(i) ** self.e) % self.n)

        return new_encrypt
