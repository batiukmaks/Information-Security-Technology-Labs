# Implementation of MD5 algorithm for hashing strings
# The code is supported with comments with explanations of the algorithm
import math

class MD5:
    def __init__(self):
        self.A = 0x67452301
        self.B = 0xefcdab89
        self.C = 0x98badcfe
        self.D = 0x10325476

        self.T = [int(abs(math.sin(i + 1)) * 2 ** 32) & 0xFFFFFFFF for i in range(64)]

        self.s = [
            [7, 12, 17, 22],
            [5, 9, 14, 20],
            [4, 11, 16, 23],
            [6, 10, 15, 21]
        ]


    def reset_state(self):
        self.A = 0x67452301
        self.B = 0xefcdab89
        self.C = 0x98badcfe
        self.D = 0x10325476

    def left_rotate(self, x, n):
        x = x & 0xFFFFFFFF
        return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

    def F(self, x, y, z):
        return (x & y) | (~x & z)

    def G(self, x, y, z):
        return (x & z) | (y & ~z)

    def H(self, x, y, z):
        return x ^ y ^ z

    def I(self, x, y, z):
        return y ^ (x | ~z)


    def preprocess(self, normal_message):
        # Convert message to bytes if it is not bytes already
        if not isinstance(normal_message, bytes):
            message = normal_message.encode('utf-8')
        else:
            message = normal_message

        original_length = len(message) * 8
        message += b'\x80'
        while (len(message) * 8) % 512 != 448:
            message += b'\x00'
        message += original_length.to_bytes(8, byteorder='little')
        return message

    def hash(self, normal_message):
        self.reset_state()

        preprocessed_message = self.preprocess(normal_message)

        # 64 bytes = 512 bits
        chunks = [preprocessed_message[i:i + 64] for i in range(0, len(preprocessed_message), 64)]

        for chunk in chunks:
            # break chunk into sixteen 32-bit words M[j], 0 ≤ j ≤ 15
            M = []
            for i in range(0, 64, 4):
                M.append(int.from_bytes(chunk[i:i + 4], byteorder='little'))

            A = self.A
            B = self.B
            C = self.C
            D = self.D

            for i in range(64):
                if 0 <= i <= 15:
                    F = self.F(B, C, D)
                    g = i
                elif 16 <= i <= 31:
                    F = self.G(B, C, D)
                    g = (5 * i + 1) % 16
                elif 32 <= i <= 47:
                    F = self.H(B, C, D)
                    g = (3 * i + 5) % 16
                elif 48 <= i <= 63:
                    F = self.I(B, C, D)
                    g = (7 * i) % 16

                dTemp = D
                D = C
                C = B
                B = B + self.left_rotate((A + F + self.T[i] + M[g]), self.s[i // 16][i % 4])
                B = B & 0xFFFFFFFF
                A = dTemp

            self.A = (self.A + A) & 0xFFFFFFFF
            self.B = (self.B + B) & 0xFFFFFFFF
            self.C = (self.C + C) & 0xFFFFFFFF
            self.D = (self.D + D) & 0xFFFFFFFF

        return self.A.to_bytes(4, byteorder='little') + \
                self.B.to_bytes(4, byteorder='little') + \
                self.C.to_bytes(4, byteorder='little') + \
                self.D.to_bytes(4, byteorder='little')

    def hexdigest(self, message):
        return self.hash(message).hex()
