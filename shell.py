"""Программа - генератор паролей с графической оболочкой"""
from tkinter import Frame, Label, TOP, Button, BOTH, Tk, Spinbox
import random
import string
from datetime import datetime
import pyperclip


class Generator:
    """Основные функции генератора паролей"""
    def __init__(self, frame):
        self.spinbox = Spinbox(frame, from_=0, to=100)

    def generator(self):
        """Функция для генерации пароля"""
        pass_symbols = string.ascii_letters + string.digits + '!@#$%&'
        pass_len = int(self)
        output_pass = ''.join(random.choice(pass_symbols) for x in range(pass_len))
        return output_pass

    def create_file(self):
        """Фунция для сохранения сгенерированного пароля в файл"""
        file = open('pass_dir/password_' +
                    str(datetime.now().strftime('%Y_%m_%d_%H_%M')) +
                    '.txt', 'tw', encoding='utf8')
        input_data = str(self)
        file.write(input_data)
        file_name = str(file)
        return file_name

    def copy_to_clipboard(self):
        """Функция для добавления сгенерированного пароля в буфер обмена"""
        pyperclip.copy(self)
        pyperclip.paste()

    @classmethod
    def spinbox(cls, frame):
        return Spinbox(frame, from_=0, to=20)


class PassGen:
    """Графическая оболочка программы генератора паролей"""

    def __init__(self, main_window):
        frame = Frame(main_window)
        frame.pack()

        """Информационный текст в окне программы"""
        self.label = Label(
            frame, text="Укажите длину пароля и \nвыберите необходимое действие")
        self.label.pack(side=TOP)

        """Выбор длины пароля"""
        self.spin = Generator.spinbox(frame)
        # self.spin = Spinbox(frame, from_=0, to=100)
        self.spin.pack(fill=BOTH)

        """Вывод сгенерированного пароля в окне программы"""
        self.output = Label(frame, fg='red', font='30')
        self.output.pack()

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
        self.output.config(
            text=Generator.generator())  # По умолчанию длина пароля составляет 6 символов

    def save_file(self):
        """Сохранение пароля в файл"""
        self.output.config(text=Generator.create_file())

    def copy_clip(self):
        """Копирование пароля в буфер обмена"""
        self.output.config(text=Generator.copy_to_clipboard())


WINDOW = Tk()
WINDOW.title("PassGen")
WINDOW.geometry('250x180')
WINDOW.resizable(width=False, height=False)
PassGen(WINDOW)
WINDOW.mainloop()
