N = int(input("Введите целое число N (> 0): "))
if N <= 0:
    print("N должно быть больше 0")
else:
    prod = 1
    for i in range(1,N + 1):
        prod = prod * (1 + i/10)
    print(prod)


   

