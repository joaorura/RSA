import sys

from maths import *


class GenerateKeys:
    def __init__(self, p, q):
        self.public = Public(p, q)
        self.private = Private(self.public.e, self.public.phi)

class Public:
    def __init__(self, p, q):
        self.n = p * q
        self.phi = Math.lcm((p - 1), (q - 1))
        # self.phi = (p - 1) * (q - 1) #also works
        self.e = Math.coprime(self.phi)

        # if one of the primes is 2
        if self.e == -1:
            sys.exit(1)

class Private:
    def __init__(self, e, phi):
        self.d = Math.mod_inverse(e, phi)
