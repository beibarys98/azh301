price_per_kg = float(input("Введите цену 1 кг конфет: "))

for weight in range(1, 11):
    cost = price_per_kg * (weight / 10)
    print(f"{weight/10:.1f} кг конфет стоит {cost:.2f}")