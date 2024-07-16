import re

def extract_numbers(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            input_string = file.read().strip()
    except FileNotFoundError:
        print(f"Помилка: '{path}' - не знайдено.")
        return [], 0 

    pattern = r'([A-Za-z\s]+),(\d+)'

    matches = re.findall(pattern, input_string)

    numbers = []

    for match in matches:
        number = int(match[1])
        numbers.append(number)

    if numbers:
        total = int(sum(numbers))
        average = int(total / len(numbers))
    else:
        total = 0
        average = 0

    return total, average

path = "exe1/name_and_salary.txt"
total, average = extract_numbers(path)


print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

