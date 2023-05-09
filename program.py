"""Программа - генератор паролей с графической оболочкой"""
from tkinter import Frame, Label, TOP, Button, BOTH, Tk, Spinbox
from generator_funcs import gen_pass, create_file, copy_to_clipboard


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
        self.generated_password = ""

    def generate(self):
        """Генерация пароля"""
        self.generated_password = gen_pass(self.spin.get())
        self.output.config(text=self.generated_password)

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
