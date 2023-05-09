import random
import string
from datetime import datetime
import pyperclip


def gen_pass(request):
    """Функция для генерации пароля"""
    pass_symbols = string.ascii_letters + string.digits + '!@#$%&'
    return ''.join(random.choice(pass_symbols) for _ in range(int(request)))


def create_file(request):
    """Функция для сохранения сгенерированного пароля в файл"""
    file_name = f'pass_dir/password_{datetime.now().strftime("%Y_%m_%d_%H_%M")}.txt'
    with open(file_name, 'w', encoding='utf8') as file:
        file.write(request)
    return file_name


def copy_to_clipboard(request):
    """Функция для добавления сгенерированного пароля в буфер обмена"""
    pyperclip.copy(request)
    pyperclip.paste()