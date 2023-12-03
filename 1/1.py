from collections import defaultdict

"""
--------------------------------
----------- PART 1 -------------
--------------------------------
"""
def function1(text: str) -> int:
    nums = []
    for char in text:
        if char.isnumeric():
            nums.append(char)
    return int(nums[0] + nums[-1])
"""
--------- END PART 1 ----------
"""

"""
--------------------------------
----------- PART 2 -------------
--------------------------------
"""
alphanumeric = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}
trie = {
}
def setup2():
    # build trie
    for alpha, number in alphanumeric.items():

        branch = trie
        # nested for loop
        for char in alpha:
            if char not in branch:
                branch[char] = {}
            branch = branch[char]

        branch["$"] = number


def function2(text: str) -> int:
    array = []
    index = 0
    generation = trie
    while index < len(text):
        char = text[index]
        if char == '\n':
            break
        if char not in generation:
            if char.isnumeric():
                array.append(char)
            generation = trie
        if char in generation:
            generation = generation[char]
        if '$' in generation:
            array.append(str(generation['$']))
            generation = trie
        else:
            index += 1

    return int(array[0] + array[-1])


"""
--------- END PART 2 ----------
"""


if __name__ == "__main__":
    # total = 0
    # with open("input.txt", 'r') as fd:
    #     for line in fd:
    #         total += (line)
    #
    # print(total)
    setup2()
    total = 0
    with open("input.txt", 'r') as fd:
        for line in fd:
            total += function2(line)
    print(total)
    pass

