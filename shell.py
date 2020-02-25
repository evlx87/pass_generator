"""Импорт используемых модулей tkinter и функций генератора паролей"""
from tkinter import Frame, Label, TOP, Button, BOTH, Tk

from generator import generator, create_file, copy_to_clipboard


class PassGen:
    """Функции оболочки генератора паролей (программы)"""

    def __init__(self, main_window):
        frame = Frame(main_window)
        frame.pack()

        """Информационный текст в окне программы"""
        self.label = Label(
            frame, text="Требуется выбрать необходимое действие")
        self.label.pack(side=TOP)

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
        self.output.config(text=generator(6))  # По умолчанию длина пароля составляет 6 символов

    def save_file(self):
        """Сохранение пароля в файл"""
        self.output.config(text=create_file())

    def copy_clip(self):
        """Копирование пароля в буфер обмена"""
        self.output.config(text=copy_to_clipboard())


WINDOW = Tk()
WINDOW.title("PassGen")
WINDOW.geometry('300x140')
WINDOW.resizable(width=False, height=False)
PassGen(WINDOW)
WINDOW.mainloop()
