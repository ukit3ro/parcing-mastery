""" q = None
for x in input('Введите строку или число:\n'):
    if x.isdigit():
        q = True
    if x.isalpha():
        q = False
print(q) """





a = float(input("Введите первое число (a): "))
b = float(input("Введите второе число (b): "))

a_rounded = round(a, 3)
b_rounded = round(b, 3)

if a_rounded >= b_rounded:
    print(True)
else:
    print(False)



