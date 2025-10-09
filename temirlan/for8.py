A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

product = 1
for i in range(A, B + 1):
    product = product * i

print("Произведение всех целых чисел от A до B включительно:", product)