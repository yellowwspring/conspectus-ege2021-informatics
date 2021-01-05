# example №1 DEMO 2021 : ( x ∨ y) ∧ ¬(y ≡ z) ∧ ¬w == 1
print("example №1:")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                # if (x | y) & (y ^ z) & (w ^ 1) == 1:
                if (x or y) and (y != z) and not w == 1:
                    print(w, x, y, z)
print("------------------------")
# 0 0 1 0
# 0 1 0 1
# 0 1 1 0
"""
you can use both equations
1. if (x | y) & (y ^ z) & (w ^ 1) == 1:

where | - bitwise OR - SUMMA (+)
| - побитовое или - сложение (+)
& - bitwise AND - multiplication (*)
& - побитовое И - умножение (*)
^ - исключающее ИЛИ - сложение по модулю

2. if (x or y) and (y != z) and not w == 1:
where or - или - сложение
and - и - умножение
not - здесь как инверсия (не w ) --> применем закон алгебра логики
"""




# example №2 : (¬a ∧ b ∧ c) ∨ (¬a ∧ b ∧ ¬c) ∨ (¬a ∧ ¬b ∧ ¬c)
# https://inf-ege.sdamgia.ru/problem?id=9788
print("example №2:")
for a in range(2):
    for b in range(2):
        for c in range(2):
            if(not a and b and c) or (not a and b and not c) or (not a and not b and not c):
                print(a, b, c)
print("----------------------")
"""
a - x, b - y, z - c

0 0 0
0 1 0
0 1 1
result inf-ege : yxz 
"""





# example №3: (x ∨ y) → (z ≡ x) == 0
#             (l ∨ m) → (n ≡ l) == 0
print("example №3:")
for l in range(2):
    for m in range(2):
        for n in range(2):
            if(not(l or m) or (n is l)) == 0:
                print(l, m, n)
print("--------------------")
"""
здесь закон алгребралогики: A → B = ¬A ∨ B
x y z 
0 1 1
1 0 0
1 1 0
"""

