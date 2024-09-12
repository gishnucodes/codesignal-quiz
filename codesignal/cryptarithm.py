def convert(map, word):
    letter_list = []
    for char in word:
        letter_list.append(map.get(char))
    return ''.join(letter_list)


def solution(crypt, solution):
    map = {}

    for row in solution:
        map[row[0]] = row[1]

    num1 = convert(map, crypt[0])
    num2 = convert(map, crypt[1])
    num3 = convert(map, crypt[2])

    # Check for leading zeroes
    if (num1.startswith('0') and len(num1) > 1) or (num2.startswith('0') and len(num2) > 1) or (
            num3.startswith('0') and len(num3) > 1):
        return False

    int_num1 = int(num1)
    int_num2 = int(num2)
    int_num3 = int(num3)

    if int_num1 + int_num2 == int_num3:
        return True
    else:
        return False

