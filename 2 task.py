# 2 задание
import itertools
def generate_combinations():
    try:
        numbers_input = input("Введите три числа через пробел: ")
        numbers = [int(x) for x in numbers_input.split()]
        if len(numbers) != 3:
            print("Ошибка: Введите ровно три числа.")
            return None
    except ValueError:
        print("Ошибка: Введены некорректные числа.")
        return None
    return list(itertools.combinations(numbers, 2))
combinations = generate_combinations()
if combinations:
    print("Сочетания из введенных чисел по 2:")
    for combination in combinations:
        print(combination)
else:
    print("Сочетания не сгенерированы из-за ошибок ввода.")