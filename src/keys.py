from maths import *

class Generate_keys:
    def __init__(self, p, q):
        self.public = Public(p, q)
        self.Private = Private()

class Public:
    def __init__(self, p, q):
        self.n = p * q
        self.phi = Math.lcm(Math, (p - 1),(q - 1))
        self.e = Math.coprime(Math, self.phi)

class Private:
    def __init__(self):
        return
