from clr_file import *


class Encrypt:
    def __init__(self, n, e):
        if type(n) != int or type(e) != int:
            raise Exception('Wrong paramater (all must be integers).')

        self.n = n
        self.e = e

    def text(self, string):
        if type(string) != str:
            raise Exception('Wrong paramater must be str, but you send a {type(string)}.')

        chars = list(string)
        new_encrypt = []
        for i in chars:
            new_encrypt.append((ord(i) ** self.e) % self.n)

        return new_encrypt

    def file(self, str_file):
        if self.n >= 2 ** 16 or self.n <= 2 ** 8:
            raise Exception('Wrong n! This must have a value greater than 2 ** 16 and a value menor than 2 ** 8.')
        if type(str_file) != str:
            raise Exception('Wrong paramater must be str, but you send a {type(string)}.')

        w_str_file = ''.join(str_file.split('.')[0] + '.clr')
        with open(str_file, 'rb') as file_read:
            clr = ClrFile(str_file, file_read, 5000)
            with open(w_str_file, 'wb') as file_write:
                file_write.write(len(str_file).to_bytes(1, byteorder='big', signed=False))
                file_write.write(bytes(str_file, 'utf-8'))

                while True:
                    bt_aux = clr.read_file()
                    if bt_aux is False:
                        break

                    for aux in bt_aux:
                        int_aux = int.from_bytes(aux, byteorder='big', signed=False)
                        int_aux = (int_aux ** self.e) % self.n
                        print(int_aux)
                        file_write.write(int_aux.to_bytes(2, byteorder='big', signed=False))
                    
                    del bt_aux

