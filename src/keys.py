import sys

from maths import *


class GenerateKeys:
    def __init__(self, p, q):
        self.public = PublicKeys(p, q)
        self.private = PrivateKeys(self.public.e, self.public.phi)

class PublicKeys:
    def __init__(self, p, q):
        self.n = p * q
        phi = Math.lcm((p - 1), (q - 1))
        # self.phi = (p - 1) * (q - 1) #also works
        self.e = Math.coprime(phi)

        # if one of the primes is 2
        if self.e == -1:
            sys.exit(1)

class PrivateKeys:
    def __init__(self, e, phi):
        self.d = Math.mod_inverse(e, phi)
