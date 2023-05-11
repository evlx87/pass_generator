"""Программа - генератор паролей с графической оболочкой"""
from tkinter import Frame, Label, TOP, Button, BOTH, Tk, Spinbox
from generator_funcs import gen_pass, create_file, copy_to_clipboard


class Shell:
    """Графическая оболочка программы генератора паролей"""
    def __init__(self, main_window):
        self.generated_password = ''

        frame = Frame(main_window)
        frame.pack()

        """Информационный текст в окне программы"""
        label = Label(frame, text="Укажите длину пароля и \nвыберите необходимое действие")
        label.pack(side=TOP)

        """Выбор длины пароля"""
        spin = Spinbox(main_window, from_=0, to=20)
        spin.pack(fill=BOTH)

        """Вывод сгенерированного пароля в окне программы"""
        output = Label(frame, fg='red', font='30')
        output.pack()

        """Кнопка для генерации пароля"""
        generate_btn = Button(
            frame,
            text="Сгенерировать новый пароль",
            fg='green',
            command=lambda: (self.update_password(output, gen_pass(spin.get()))))
        generate_btn.pack(fill=BOTH)

        """Кнопка для сохранения пароля в файл"""
        save_btn = Button(
            frame,
            text="Сохранить в файл",
            command=lambda: (create_file(self.generated_password), self.update_label(output)))
        save_btn.pack(fill=BOTH)

        """Кнопка для копирования сгенерированного пароля в буфер обмена"""
        copy_btn = Button(
            frame,
            text="Скопировать пароль",
            command=lambda: output.config(text=copy_to_clipboard(self.generated_password)))
        copy_btn.pack(fill=BOTH)

    def update_password(self, label, password):
        self.generated_password = password
        self.update_label(label)

    def update_label(self, label):
        label.config(text=self.generated_password)


WINDOW = Tk()
WINDOW.title("PassGen")
WINDOW.geometry('250x180')
WINDOW.resizable(width=False, height=False)
Shell(WINDOW)
WINDOW.mainloop()
