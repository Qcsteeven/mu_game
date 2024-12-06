import json
import os


# Класс для адаптации данных из конфигурационного файла
class Adapter:
    @staticmethod
    def adapt(path=None):
        """
        Загружает и адаптирует данные из конфигурационного файла.

        :param path: Путь к файлу конфигурации (по умолчанию `config.json` в текущем каталоге)
        :return: Список опций, определённых в конфигурации
        """
        # Получение текущего каталога, где находится данный файл
        current_dir = os.path.dirname(__file__)
        # Установка пути к файлу конфигурации (если путь не задан, используется 'config.json')
        path = os.path.join(current_dir, 'config.json')

        # Открытие конфигурационного файла для чтения
        with open(path, "r") as rfile:
            # Загрузка содержимого файла как JSON
            data = json.load(rfile)

        # Возврат значения ключа "options" из загруженного JSON
        return data["options"]
