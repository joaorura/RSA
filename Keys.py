import random
from MatFunctions import MatFunctions


class Keys:
    @staticmethod
    def public(phi, n):
        e = 2
        while MatFunctions.mdc(e, n) != 1:
            e += 1

            if e >= phi:
                return -1

        return e

    @staticmethod
    def private(e, phi):
        d = phi * 2
        d += 1
        d //= e

        return d
