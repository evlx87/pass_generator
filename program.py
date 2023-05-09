"""Программа - генератор паролей с графической оболочкой"""
import random
import string
from datetime import datetime
import pyperclip
from tkinter import Frame, Label, TOP, Button, BOTH, Tk, Spinbox


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


class Shell:
    """Графическая оболочка программы генератора паролей"""

    def __init__(self, main_window):
        self.frame = Frame(main_window)
        self.frame.pack()
        """Информационный текст в окне программы"""
        self.label = Label(
            self.frame,
            text="Укажите длину пароля и \nвыберите необходимое действие")
        self.label.pack(side=TOP)
        """Выбор длины пароля"""
        self.spin = Spinbox(main_window, from_=0, to=20)
        self.spin.pack(fill=BOTH)
        """Вывод сгенерированного пароля в окне программы"""
        self.output = Label(self.frame, fg='red', font='30')
        self.output.pack()
        """Кнопка для генерации пароля"""
        self.generate_btn = Button(
            self.frame,
            text="Сгенерировать новый пароль",
            fg='green',
            command=self.generate)
        self.generate_btn.pack(fill=BOTH)

        """Кнопка для сохранения пароля в файл"""
        self.save_btn = Button(
            self.frame,
            text="Сохранить в файл",
            command=self.save_file)
        self.save_btn.pack(fill=BOTH)

        """Кнопка для копирования сгенерированного пароля в буфер обмена"""
        self.copy_btn = Button(
            self.frame,
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
