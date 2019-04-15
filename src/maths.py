import math

class Math:
    "Auxiliary mathematical functions"

    @staticmethod
    def is_prime(n):
        if n % 2 == 0 and n > 2:
            return False

        factors = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                factors += 1

        if factors == 1:#prime
            return True
        else:
            return False

    def gcd(self, n, m):#mdc
        if n > m:
            m, n = n, m

        while True:
            temp = n % m
            if temp == 0:
                return m
            n = m
            m = temp

    def lcm(self, p, q):#mmc
        return (abs(p * q) // self.gcd(self, p, q))

    def coprime(self, phi):
        if phi == 2:
            return -1
        for e in range(2, phi):
            if self.gcd(self, e, phi) == 1:
                return e

    def mod_inverse(x,y):
        def eea(a,b):
            if b == 0:
                return (1,0)
            (q,r) = (a // b, a % b)
            (s,t) = eea(b,r)
            return (t, s-(q*t) )

        inv = eea(x,y)[0]
        if inv < 1: inv += y #we only want positive values
        return inv
