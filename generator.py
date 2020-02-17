import string
import random
from datetime import datetime


def generator(pass_len):
    pass_symbols = string.ascii_letters + string.digits + '!@#$%&'
    pass_len = int(pass_len)
    new_pass = ''.join(random.choice(pass_symbols) for x in range(pass_len))

    return new_pass


# def create_file(request):
#     new_pass_file = open('pass_dir/password_' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.txt',
#                          'tw',
#                          encoding='utf8')
#     input_data = str(request)
#     new_pass_file.write(input_data)
#     file_name = str(new_pass_file)
#
#     return file_name


print(generator(input("Укажите желаемую длину пароля(число): ")))
