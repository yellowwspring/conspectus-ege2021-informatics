"""
ПРИМЕР №1: (с ИЛИ)
Рассматривается множество целых чисел, принадлежащих числовому отрезку [5883; 15906],
которые делятся на 9 ИЛИ 23 и не делятся на 13, 18, 19, 22.
Найти кол-во  таких чисел и МАКС из них.
ОБРАТИТЬ ВНИМАНИЕ НА СКОБКИ!
"""
# example №1:

y = []

for u in range(5883, 15906):
    if ((u % 9 == 0) or (u % 23 == 0)) and u % 13 != 0 and u % 18 != 0 and u % 19 != 0 and u % 22 != 0:
        y.append(u)

print(len(y), max(y))  # 810 15893



"""
Рассматривается множество целых чисел, принадлежащих числовому отрезку [3521; 13019],
которые делятся на 9 И 15 и не делятся на 6, 12, 17, 21.
Найти кол-во  таких чисел и минимальное из них.
"""
# example №2:

f = []

for i in range(3521, 13019):
    if i % 9 == 0 and i % 15 == 0 and i % 6 != 0 and i % 12 != 0 and i % 17 != 0 and i % 21 != 0:
        f.append(i)

print(len(f), min(f)) # 85 3555