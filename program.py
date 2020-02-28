"""Программа - генератор паролей с графической оболочкой"""
from tkinter import Frame, Label, TOP, Button, BOTH, Tk, Spinbox
import random
import string
from datetime import datetime
import pyperclip


def gen_pass(request):
    """Функция для генерации пароля"""
    pass_symbols = string.ascii_letters + string.digits + '!@#$%&'
    output_pass = ''.join(random.choice(pass_symbols) for x in range(int(request)))
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


def spinbox(frame):
    """Функция выбора длины пароля"""
    spin = Spinbox(frame, from_=5, to=20)
    return spin


class Shell:
    """Графическая оболочка программы генератора паролей"""

    def __init__(self, main_window):
        frame = Frame(main_window)
        frame.pack()

        """Информационный текст в окне программы"""
        self.label = Label(
            frame, text="Укажите длину пароля и \nвыберите необходимое действие")
        self.label.pack(side=TOP)

        """Выбор длины пароля"""
        self.spin = spinbox(frame)
        self.spin.pack(fill=BOTH)

        """Вывод сгенерированного пароля в окне программы"""
        self.output = Label(frame, fg='red', font='30')
        self.output.pack(fill=BOTH)

        """Кнопка для генерации пароля"""
        self.generate_btn = Button(
            frame,
            text="Сгенерировать новый пароль",
            fg='green',
            command=self.generate)
        self.generate_btn.pack(fill=BOTH)

        """Кнопка для сохранения пароля в файл"""
        self.save_btn = Button(
            frame,
            text="Сохранить в файл",
            command=self.save_file)
        self.save_btn.pack(fill=BOTH)

        """Кнопка для копирования сгенерированного пароля в буфер обмена"""
        self.copy_btn = Button(
            frame,
            text="Скопировать пароль",
            command=self.copy_clip)
        self.copy_btn.pack(fill=BOTH)

    def generate(self):
        """Генерация пароля"""
        self.output.config(text=gen_pass(self.spin.get()))

    def save_file(self):
        """Сохранение пароля в файл"""
        self.output.config(text=create_file(self.output['text']))

    def copy_clip(self):
        """Копирование пароля в буфер обмена"""
        self.output.config(text=copy_to_clipboard(self.output['text']))


WINDOW = Tk()
WINDOW.title("PassGen")
WINDOW.geometry('250x180')
WINDOW.resizable(width=False, height=False)
Shell(WINDOW)
WINDOW.mainloop()
