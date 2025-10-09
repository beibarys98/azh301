A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A < B:
    for num in range(A, B + 1):
        print(num, end=' ')
    N = B - A + 1
    print(f"\nКоличество чисел: {N}")
else:
    print("Ошибка: A должно быть меньше B.")