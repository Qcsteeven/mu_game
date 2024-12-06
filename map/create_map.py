import json
import random


# Класс для генерации двумерных массивов с заданной структурой
class PatCreator:
    @staticmethod
    def create_2d_array(rows, cols, d_count):
        """
        Создаёт двумерный массив для представления карты игры.

        :param rows: Количество строк в массиве
        :param cols: Количество столбцов в массиве
        :param d_count: Количество комнат типа "d" (темницы)
        :return: Двумерный массив с заданной структурой
        """
        # Инициализация массива. Все клетки изначально обозначены как пустые ('-')
        array = [['-' for _ in range(cols)] for _ in range(rows)]

        # Установка фиксированных комнат:
        # 's' - стартовая комната (в верхнем левом углу)
        array[0][0] = 's'
        # 'a' - оружейная комната (рядом со стартовой)
        array[0][1] = 'a'
        # 'B' - комната босса (в правом нижнем углу)
        array[rows - 1][cols - 1] = 'B'

        # Список доступных позиций для размещения других типов комнат
        positions = [(i, j) for i in range(rows) for j in range(cols) if array[i][j] == '-']

        # Размещение комнат типа "d" (темницы)
        for _ in range(d_count):
            # Случайный выбор доступной позиции из списка
            i, j = random.choice(positions)
            # Помещение темницы на выбранную позицию
            array[i][j] = 'd'
            # Удаление выбранной позиции из доступных
            positions.remove((i, j))

        # Возвращаем готовый массив
        return array
