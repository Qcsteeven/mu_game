import json
import random


class PatCreator:
    @staticmethod
    def create_2d_array(rows, cols, d_count):

        array = [['-' for _ in range(cols)] for _ in range(rows)]

        array[0][0] = 's'
        array[0][1] = 'a'
        array[rows - 1][cols - 1] = 'B'

        positions = [(i, j) for i in range(rows) for j in range(cols) if array[i][j] == '-']

        for _ in range(d_count):
            i, j = random.choice(positions)
            array[i][j] = 'd'
            positions.remove((i, j))

        return array



      
