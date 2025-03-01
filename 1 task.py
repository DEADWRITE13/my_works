# 1 задание
def count_three_digit_numbers():
    num_digits = int(input("Введите количество доступных цифр : "))
    if not (1 <= num_digits <= 9):
        print("Ошибка")
        return None
    return num_digits ** 3
result = count_three_digit_numbers()
if result is not None:
    print(f"Количество трехзначных чисел, которые можно составить: {result}")
else:
    print("Невозможно вычислить.")