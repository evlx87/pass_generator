import random
import string
import os
from datetime import datetime
import secrets
import pyperclip
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
import sys
import logging

# Настройка логирования
os.makedirs('logs', exist_ok=True)  # Создаём папку для логов
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/password_generator.log', encoding='utf-8'),
        logging.StreamHandler()  # Вывод в консоль
    ]
)
logger = logging.getLogger(__name__)


class PasswordGenerator:
    """
    Класс для генерации паролей.
    """

    def __init__(self, length):
        self.length = length
        self.generated_password = ''
        self.password_saved = False

    def generate_password(self):
        """
        Генерирует случайный пароль заданной длины.
        :return: Сгенерированный пароль
        """
        if self.length < 1:
            logger.error("Длина пароля должна быть больше 0")
            raise ValueError("Длина пароля должна быть больше 0")

        letters = string.ascii_letters
        digits = string.digits
        special_chars = '!@#$%&*()_+-=[]{}|;:,./<>?'
        all_chars = letters + digits + special_chars

        password = []
        password.append(secrets.choice(letters))
        password.append(secrets.choice(digits))
        password.append(secrets.choice(special_chars))

        for _ in range(self.length - 3):
            password.append(secrets.choice(all_chars))

        random.shuffle(password)
        generated_passwords = set()
        while True:
            password_str = ''.join(password)
            if password_str not in generated_passwords:
                generated_passwords.add(password_str)
                self.generated_password = password_str
                logger.info(
                    f"Сгенерирован пароль длиной {self.length}: {password_str}")
                return password_str
            random.shuffle(password)

    def is_password_saved(self):
        """
        Проверяет, был ли пароль сохранен.
        :return: True, если пароль сохранен, иначе False
        """
        return self.password_saved

    def set_password_saved(self, value):
        """
        Устанавливает флаг, был ли пароль сохранен.
        :param value: True, если пароль сохранен, иначе False
        """
        self.password_saved = value


class FileSaver:
    """
    Класс для сохранения паролей в файл.
    """

    def __init__(self):
        self.pass_dir = 'pass_dir'
        self.file_name = f'{self.pass_dir}/password_{datetime.now().strftime("%Y_%m_%d")}.txt'

    def create_file(self, password):
        """
        Сохраняет сгенерированный пароль в файл.
        :param password: Пароль для сохранения
        :return: Путь к созданному файлу
        """
        try:
            os.makedirs(self.pass_dir, exist_ok=True)
            if os.path.exists(self.file_name):
                with open(self.file_name, 'a', encoding='utf8') as file:
                    file.write(password + '\n')
            else:
                with open(self.file_name, 'w', encoding='utf8') as file:
                    file.write(password + '\n')
            logger.info(f"Пароль сохранён в файл: {self.file_name}")
            return self.file_name
        except Exception as e:
            logger.error(f"Ошибка при сохранении файла: {str(e)}")
            raise


class PasswordGeneratorUI(QDialog):
    """
    Графический интерфейс программы генератора паролей на основе PyQt5.
    """

    def __init__(self):
        super().__init__()
        # Загружаем UI из файла
        uic.loadUi('gui/genQt.ui', self)
        logger.info("Инициализация графического интерфейса")

        # Инициализация объектов
        self.password_generator = None

        # Подключение сигналов кнопок
        self.pushButton.clicked.connect(self.generate_password)
        self.pushButton_2.clicked.connect(self.save_password)
        self.pushButton_3.clicked.connect(self.copy_password)

    def generate_password(self):
        """
        Генерирует новый пароль и отображает его.
        """
        try:
            length = self.spinBox.value()
            if length < 3:
                self.password_label.setText(
                    "Длина пароля должна быть не менее 3!")
                logger.warning("Попытка генерации пароля с длиной менее 3")
                return
            self.password_generator = PasswordGenerator(length)
            password = self.password_generator.generate_password()
            self.password_label.setText(password)
            self.password_generator.set_password_saved(False)
            logger.info("Пароль успешно отображён в интерфейсе")
        except ValueError as e:
            self.password_label.setText(
                "Длина пароля должна быть положительным числом!")
            logger.error(f"Ошибка генерации пароля: {str(e)}")

    def save_password(self):
        """
        Сохраняет пароль в файл.
        """
        if self.password_generator and not self.password_generator.is_password_saved():
            try:
                file_saver = FileSaver()
                file_path = file_saver.create_file(
                    self.password_generator.generated_password)
                file_name = os.path.basename(file_path)
                self.password_label.setText(
                    f"Пароль сохранен в файл:\n{file_name}")
                self.password_generator.set_password_saved(True)
                logger.info("Пароль успешно сохранён")
            except Exception as e:
                self.password_label.setText("Ошибка при сохранении файла!")
                logger.error(f"Ошибка при сохранении пароля: {str(e)}")
        else:
            self.password_label.setText("Сначала сгенерируйте пароль!")
            logger.warning("Попытка сохранить пароль без его генерации")

    def copy_password(self):
        """
        Копирует пароль в буфер обмена.
        """
        if self.password_generator and self.password_generator.generated_password:
            try:
                pyperclip.copy(self.password_generator.generated_password)
                self.password_label.setText(
                    "Пароль скопирован в буфер обмена!")
                logger.info("Пароль скопирован в буфер обмена")
            except Exception as e:
                self.password_label.setText("Ошибка при копировании пароля!")
                logger.error(f"Ошибка при копировании пароля: {str(e)}")
        else:
            self.password_label.setText("Сначала сгенерируйте пароль!")
            logger.warning("Попытка копирования пароля без его генерации")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGeneratorUI()
    window.show()
    logger.info("Приложение запущено")
    sys.exit(app.exec_())
