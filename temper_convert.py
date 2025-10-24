def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Выберите конвертацию:")
print("1. Цельсий → Фаренгейт")
print("2. Фаренгейт → Цельсий")

choice = input("Ваш выбор (1 или 2): ")

if choice == '1':
    temp = float(input("Введите температуру в Цельсиях: "))
    result = celsius_to_fahrenheit(temp)
    print(f"{temp}°C = {result:.1f}°F")
elif choice == '2':
    temp = float(input("Введите температуру в Фаренгейтах: "))
    result = fahrenheit_to_celsius(temp)
    print(f"{temp}°F = {result:.1f}°C")
else:
    print("Неверный выбор!")
