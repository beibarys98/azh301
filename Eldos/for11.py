
N = int(input("Введите целое число N (> 0): "))
if N <= 0:
    print("N должно быть больше 0")
else:
    sum = 0.0
    for i in range(N,2*N + 1):
        sum = sum + i**2
    print(sum)