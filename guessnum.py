import random

number = random.randint(1, 100)
attempts = 0

print("Я загадал число от 1 до 100. Попробуй угадать!")

while True:
    guess = int(input("Твоя догадка: "))
    attempts += 1
    
    if guess < number:
        print("Слишком маленькое!")
    elif guess > number:
        print("Слишком большое!")
    else:
        print(f"Поздравляю! Ты угадал за {attempts} попыток.")
        break
