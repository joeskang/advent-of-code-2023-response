"""
only 12 red cubes, 13 green cubes, and 14 blue cubes
"""
from collections import defaultdict
import math
count = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def f1(line: str) -> bool:
    line = line.replace(',', '')
    line = ' '.join(line.split()[2:])
    for section in line.split(';'):
        word_list = section.split()
        line_count = defaultdict(int)
        while word_list:
            line_count[word_list.pop()] += int(word_list.pop())

        for k, v in line_count.items():
            if count[k] < v:
                return False
    return True

def f2(line: str) -> int:
    min_count = {
        "red": -math.inf,
        "blue": -math.inf,
        "green": -math.inf
    }
    line = line.replace(',', '')
    line = ' '.join(line.split()[2:])
    for section in line.split(';'):
        word_list = section.split()
        line_count = defaultdict(int)
        while word_list:
            line_count[word_list.pop()] += int(word_list.pop())

        for k, v in line_count.items():
            min_count[k] = max(min_count[k], v)

    power = 1
    for num in min_count.values():
        power *= num
    return power

if __name__ == "__main__":
    id_sum = 0
    with open("input.txt", 'r') as fobj:
        for index, line in enumerate(fobj):
            id_sum += f2(line)
    print(id_sum)

