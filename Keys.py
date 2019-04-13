import random
import MatFunctions


class Keys:
    @staticmethod
    def public(phi, n):
        i = 2
        while MatFunctions.mdc(i, n) != 1 and i < phi:
            i += 1

        return i

    @staticmethod
    def private(e, phi, a, b):
        d = phi * random.getrandbits(random.randint(a, b))
        d += 1
        d /= e

        return e
