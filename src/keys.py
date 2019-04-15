from maths import *

class Public:
    def __init__(self, p, q):
        self.n = p * q
        self.phi = Math.lcm(Math, (p - 1),(q - 1))
        self.e = Math.coprime(Math, self.phi)
