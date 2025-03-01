#1 задание
def count_three_digit_numbers():
    num_digits = int(input("Введите количество доступных цифр: "))
    if num_digits <= 0:
        print("Ошибка: Количество цифр должно быть положительным числом.")
        return None
    if num_digits is not None:
        return num_digits ** 3
    else:
        return None
result = count_three_digit_numbers()
if result is not None:
    print("Количество  чисел, которые можно составить:", result)
else:
    print("Невозможно вычислить.")