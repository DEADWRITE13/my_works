# 3 задани е
import itertools

def generate_schedules():
    subjects = ["Математика", "Информатика", "Русский язык"]
    combinations_with_replacement = itertools.combinations_with_replacement(subjects, 2)
    all_schedules = []
    for combination in combinations_with_replacement:
        if combination[0] != combination[1]:
            all_schedules.append((combination[0], combination[1]))
            all_schedules.append((combination[1], combination[0]))
        else:
            all_schedules.append((combination[0], combination[1]))
    return all_schedules
schedules = generate_schedules()
print("Варианты расписания:")
for schedule in schedules:
    print(schedule)