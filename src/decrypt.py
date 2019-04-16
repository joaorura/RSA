from clr_file import *


class Decrypt:
    def __init__(self, n, d):
        if type(n) != int or type(d) != int:
            raise Exception('Wrong paramaters n and d (all must be integers).')
        self.n = n
        self.d = d

    def text(self, dec_list):
        if type(dec_list) != list:
            return -1

        new_encrypt = []
        for i in dec_list:
            new_encrypt.append((i ** self.d) % self.n)

        return new_encrypt

    def file(self, str_file):
        if self.n >= 2 ** 16 or self.n <= 2 ** 8:
            raise Exception('Wrong n! This must have a value greater than 2 ** 16 and a value menor than 2 ** 8.')
        if type(str_file) != str:
            raise Exception('Wrong paramater must be str, but you send a {type(string)}.')
        str_aux = str_file.split('.')
        if str_aux[1] != 'clr' or len(str_aux) > 2:
            raise Exception('Wrong parameter! It should be a str containing a single extension (.clr).\n' +
                            f'\tString send: {str_file}')

        with open(str_file, 'rb') as read_file:
            clr = ClrFile(str_file, read_file, 5000)
            header = clr.read_header()
            with open(header[1], 'wb') as file_write:
                while True:
                    bt_aux = clr.read_file()
                    if bt_aux is False:
                        break

                    i = 0
                    exit_bt = []
                    for aux in bt_aux:
                        if i == 0:
                            bt = aux
                            i += 1
                        if i == 1:
                            bt += aux
                            i = 0
                            int_aux = int.from_bytes(bt, byteorder='big', signed=False)
                            exit_bt.append((int_aux ** self.d) % self.n)

                    for aux in exit_bt:
                        print(aux)
                        file_write.write(aux.to_bytes(1, byteorder='big', signed=False))

                    del bt_aux
                    del exit_bt
