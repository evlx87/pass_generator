"""Импорты"""
import random
import string
from datetime import datetime
import pyperclip


NEW_PASS = []  # Временно созданная переменная для тестов


def generator(request):
    """Функция для генерации пароля"""
    pass_symbols = string.ascii_letters + string.digits + '!@#$%&'
    pass_len = int(request)
    output_pass = ''.join(random.choice(pass_symbols) for x in range(pass_len))
    NEW_PASS.append(output_pass)
    return output_pass


def create_file(request):
    """Фунция для сохранения сгенерированного пароля в файл"""
    file = open('pass_dir/password_' +
                str(datetime.now().strftime('%Y_%m_%d_%H_%M')) +
                '.txt', 'tw', encoding='utf8')
    input_data = str(request)
    file.write(input_data)
    file_name = str(file)
    return file_name


def copy_to_clipboard(request):
    """Функция для добавления сгенерированного пароля в буфер обмена"""
    pyperclip.copy(request)
    pyperclip.paste()
