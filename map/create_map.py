import json
import random


def create_2d_array(rows, cols, d_count, priz):
    array = [['' for _ in range(cols)] for _ in range(rows)]

    array[0][0] = 's'
    array[0][1] = 'a'

    array[rows - 1][cols - 1] = 'B'

    for i in range(rows):
        for j in range(cols):
                if array[i][j] == '':
                    array[i][j] = random.choice(['-', 'd', 'p'])
                    if(array[i][j] == 'd'):
                        d_count -= 1
                    if(array[i][j] == 'p'):
                        priz -= 1
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
