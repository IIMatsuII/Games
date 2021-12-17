from random import *
condition = True
while condition:
    conter = 0
    n = int(input("Введите границу: "))
    num = randint(1, n)
    print("Добро пожаловать в числовую угадайку: ")

    def is_valid(num):
        if num.isdigit():
            num = int(num)
            if 1 <= num <= 100:
                return True
            else:
                return False

    while True:
        numbers = input(f"Введите число от 1 до {n}: ")
        if is_valid(numbers):
            numbers = int(numbers)
            if numbers < num:
                print("Ваше число меньше заданного, попробуйте еще разок: ")
                conter += 1
            elif numbers > num:
                print("Ваше число больше заданного, попробуйте еще разок")
                conter += 1
            elif numbers == num:
                print("Вы угадали, поздравляем:")
                break
            else:
                print("Может быть введем число от 1 до 100 :")
    print(f"Вы пытались угадать: {conter} раз")
    print("Хотетие еще раз сыграть: ")

print(f"Спасибо, что играли в числовую угадайку. Еще увидимся...")





