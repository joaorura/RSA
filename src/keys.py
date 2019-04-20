import sys

from maths import *


class GenerateKeys:
    def __init__(self, p, q, e = -1):
        self.public = PublicKeys(p, q, e)
        self.private = PrivateKeys(self.public.e, self.public.phi)

class PublicKeys:
    def __init__(self, p, q , e = -1):
        self.n = p * q
        self.phi = Math.lcm((p - 1), (q - 1))
        # self.phi = (p - 1) * (q - 1) #also works
        
        if e == -1:
            self.e = Math.coprime(self.phi)
            # if one of the primes is 2
            if self.e == -1:
                sys.exit(1)
        else:
            self.e = e

class PrivateKeys:
    def __init__(self, e, phi):
        self.d = Math.mod_inverse(e, phi)
