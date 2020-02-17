import string
import random


def generator(pass_len):
    pass_symbols = string.ascii_letters + string.digits + '!@#$%&'
    pass_length = int(pass_len)
    new_pass = ''.join(random.choice(pass_symbols) for x in range(pass_length))

    return new_pass

