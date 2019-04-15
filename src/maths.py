class Math:
    "Auxiliary mathematical functions"

    @staticmethod
    def is_prime(n):
        factors = 0
        for i in range(1, n):
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
        for e in range(2, phi):
            if self.gcd(self, e, phi) == 1:
                return e
