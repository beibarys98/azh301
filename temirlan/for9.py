A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A >= B:
    print("A должно быть меньше B")
else:
    total = 0
    for i in range(A, B + 1):
        total = total + i ** 2
    print("Сумма квадратов:", total)