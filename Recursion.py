def test_func(*params):
    print(params)
print("Задание 1. Произвольное число параметров")
test_func("Привет", 25, True)
print()

def factorial_(n):
    if n == 1:
        return 1
    else:
        return n * factorial_(n-1)

print("Задание 2. Рекурсия")
n = int(input("Введите число n: "))
print(factorial_(n))