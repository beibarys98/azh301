A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

numbers = []
for num in range(B - 1, A, -1):
    numbers.append(num)

for num in numbers:
    print(num)

print("Количество чисел N:", len(numbers))