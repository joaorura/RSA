import math


class Math:
    # Auxiliary mathematical functions

    @staticmethod
    def is_prime(n):
        if n % 2 == 0 and n > 2:
            return False

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        # prime
        return True

    @staticmethod
    # mdc
    def gcd(n, m):
        if n > m:
            m, n = n, m

        while True:
            temp = n % m
            if temp == 0:
                return m
            n = m
            m = temp

    @staticmethod
    # mmc
    def lcm(p, q):
        return abs(p * q) // Math.gcd(p, q)

    @staticmethod
    def coprime(phi):
        if phi == 2:
            return -1
        for e in range(2, phi):
            if Math.gcd(e, phi) == 1:
                return e

    @staticmethod
    def mod_inverse(x, y):
        def eea(a, b):
            if b == 0:
                r = (1, 0)
                return r
            (q, r) = (a // b, a % b)
            (s, t) = eea(b, r)

            r = (t, s - (q * t))
            return r

        inv = eea(x, y)[0]
        # we only want positive values
        if inv < 1:
            inv += y

        return inv
