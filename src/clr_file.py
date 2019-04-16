class ClrFile:
    def __init__(self, str_aux, file, buffer_size):
        if buffer_size <= 0:
            raise Exception("buffer_size <= 0. The buffer must be greater than 0")

        self.str_file = str_aux
        self.file = file
        self.bfs = buffer_size

    def read_header(self):
        bt_aux = self.file.read(1)
        if bt_aux is None:
            raise Exception(f"The file {self.str_file} not it's a file clr.")

        size_header = int.from_bytes(bt_aux, byteorder='big', signed=False)
        bt_aux = self.file.read(size_header)
        if bt_aux is None or len(bt_aux) < size_header:
            raise Exception(f"The file {self.str_file} not it's a file clr.")
        
        decrypt_name = bt_aux.decode('utf-8')
        t = (size_header, decrypt_name)
        return t

    def read_file(self):
        i = 0
        buffer = []
        while True:
            byte_aux = self.file.read(1)
            if byte_aux == b'':
                if len(buffer) == 0:
                    return False
                else:
                    return buffer

            buffer.append(byte_aux)
            i += len(byte_aux)
            if i >= self.bfs:
                return buffer
