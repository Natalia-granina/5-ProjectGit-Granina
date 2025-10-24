def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м): "))

bmi = calculate_bmi(weight, height)
print(f"Ваш индекс массы тела: {bmi}")
