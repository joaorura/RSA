import  random


class MatFunctions:
    @staticmethod
    def phi(p, q):
        return (p - 1) * (q - 1)

    @staticmethod
    def mdc(a, b):
        if a < b:
            a,b = b,a

        while True:
            mod = a % b
            if mod == 0:
                break

            a = b
            b = mod

        return b

class Keys:
    @staticmethod
    def public(phi, n):
        i = 2
        while MatFunctions.mdc(i, n) != 1 and i < phi:
            i += 1

        return i

    @staticmethod
    def private(e, phi):
        d = phi * random.random()



class Encrypt:

    def __init__(self, p, q):
        self.n = p * q
        self.phi = MatFunctions.phi(p, q)
        self.e = Keys.public(self.phi, self.n)
        self.d = Keys.private()


    def generate_keys(self):
        Keys.public(self.p, self.q)
