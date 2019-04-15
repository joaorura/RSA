class MatFunctions:
    @staticmethod
    def phi(p, q):
        return (p - 1) * (q - 1)

    @staticmethod
    def mdc(a, b):
        if a < b:
            a, b = b, a

        while True:
            mod = a % b
            if mod == 0:
                break

            a = b
            b = mod

        print(f'')
        return b
