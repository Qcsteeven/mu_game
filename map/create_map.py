import json
import random


def create_2d_array(rows, cols, d_count, priz):

    array = [['-' for _ in range(cols)] for _ in range(rows)]

    array[0][0] = 's'
    array[0][1] = 'a'
    array[rows - 1][cols - 1] = 'B'

    positions = [(i, j) for i in range(rows) for j in range(cols) if array[i][j] == '-']

    for _ in range(d_count):
        i, j = random.choice(positions)
        array[i][j] = 'd'
        positions.remove((i, j))

    for _ in range(priz):
        i, j = random.choice(positions)
        array[i][j] = 'p'
        positions.remove((i, j))

    return array


def print_array(array):
    for row in array:
        print(' '.join(row))


with open("config.json", "r") as file:
    data = json.load(file)

rows = data["options"]["rows"]
cols = data["options"]["cols"]
d_count = data["options"]["d_count"]
priz = data["options"]["priz"]

array = create_2d_array(rows, cols, d_count, priz)
print_array(array)
