import random
import string
import os
from datetime import datetime
import secrets
import pyperclip
from tkinter import Frame, Label, TOP, Button, BOTH, Tk, Spinbox
from tkinter.messagebox import showinfo


# Функция для генерации пароля
def gen_pass(length):
    """
    Генерирует случайный пароль заданной длины.

    :param length: Длина пароля
    :return: Сгенерированный пароль
    """
    if length < 1:
        raise ValueError("Длина пароля должна быть больше 0")

    pass_symbols = string.ascii_letters + string.digits + '!@#$%&*()_+-=[]{}|;:,./<>?'
    return ''.join(secrets.choice(pass_symbols) for _ in range(length))


# Функция для сохранения сгенерированного пароля в файл
def create_file(password):
    """
    Сохраняет сгенерированный пароль в файл.

    :param password: Пароль для сохранения
    :return: Путь к созданному файлу
    """
    os.makedirs('pass_dir', exist_ok=True)  # Создаем папку, если она не существует
    file_name = f'pass_dir/password_{datetime.now().strftime("%Y_%m_%d_%H_%M")}.txt'
    with open(file_name, 'w', encoding='utf8') as file:
        file.write(password)
    return file_name


# Функция для добавления сгенерированного пароля в буфер обмена
def copy_to_clipboard(password):
    """
    Копирует пароль в буфер обмена.

    :param password: Пароль для копирования
    """
    pyperclip.copy(password)


class Shell:
    """
    Графическая оболочка программы генератора паролей.
    """

    def __init__(self, main_window, original_height):
        self.generated_password = ''  # Переменная для хранения сгенерированного пароля
        self.original_height = original_height  # Передача начальной высоты окна
        self.expanded_height = 320
        self.window_height = self.original_height

        frame = Frame(main_window)
        frame.pack()

        label = Label(frame, text="Укажите длину пароля\nи выберите необходимое действие")
        label.pack(side=TOP, pady=(0, 10))  # Добавлен отступ снизу 10 пикселей

        button_width = 28  # Ширина кнопок

        # Поле для выбора длины пароля
        self.spin = Spinbox(main_window, from_=6, to=20, width=button_width)
        self.spin.pack(pady=10)

        self.password_label = Label(frame, fg='black', font='Helvetica 14 bold')
        self.password_label.pack()

        # Метка для сообщений
        self.status_label = Label(frame, fg='blue', font='Arial 11 italic')
        self.status_label.pack()

        # Кнопки действий
        generate_btn = Button(
            frame,
            text="Сгенерировать новый пароль",
            fg='green',
            width=button_width,
            command=self.update_password
        )
        generate_btn.pack(pady=(15, 5))  # Отступы сверху и снизу

        save_btn = Button(
            frame,
            text="Сохранить в файл",
            width=button_width,
            command=self.save_password
        )
        save_btn.pack(pady=5)

        copy_btn = Button(
            frame,
            text="Скопировать пароль",
            width=button_width,
            command=self.copy_password
        )
        copy_btn.pack(pady=5)

    def update_password(self):
        """
        Обновляет сгенерированный пароль.
        """
        try:
            length = int(self.spin.get())  # Получение длины пароля из поля ввода
            self.generated_password = gen_pass(length)
            self.password_label.config(text=self.generated_password)  # Обновление отображаемого пароля
            self.status_label.config(text="Пароль сгенерирован!")  # Уведомление
        except ValueError:
            self.status_label.config(text="Длина пароля должна быть положительным целым числом!")

    def save_password(self):
        """
        Сохраняет пароль в файл.
        """
        if self.generated_password:
            file_path = create_file(self.generated_password)
            # Извлекаем только имя файла из полного пути
            file_name = os.path.basename(file_path)
            # Формируем сообщение с двумя строками
            message = f"Пароль сохранен в файл:\n{file_name}"
            self.status_label.config(text=message)

            # Временное увеличение высоты окна
            self.window_height = self.expanded_height
            self.resize_window()

            # Возвращаемся к первоначальной высоте окна через 3 секунды
            self.after(3000, lambda: self.set_original_size())
        else:
            self.status_label.config(text="Сначала сгенерируйте пароль!")

    def set_original_size(self):
        self.window_height = self.original_height
        self.resize_window()

    def resize_window(self):
        self.master.geometry(f'300x{self.window_height}')

    def copy_password(self):
        """
        Копирует пароль в буфер обмена.
        """
        if self.generated_password:
            copy_to_clipboard(self.generated_password)
            self.status_label.config(text="Пароль скопирован в буфер обмена!")
        else:
            self.status_label.config(text="Сначала сгенерируйте пароль!")


if __name__ == "__main__":
    WINDOW = Tk()
    WINDOW.title("PassGen")
    original_height = 290
    WINDOW.geometry(f'300x{original_height}')  # Исходная геометрия окна
    WINDOW.resizable(width=False, height=False)
    app = Shell(WINDOW, original_height)
    WINDOW.mainloop()
