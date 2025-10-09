A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A < B:
    total = sum(range(A, B + 1))
    print("Сумма всех целых чисел от A до B включительно:", total)
else:
    print("Ошибка: A должно быть меньше B.")