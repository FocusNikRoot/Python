height = int(input("Введите высоту прямоугольника: "))
weignt = int(input("Введите ширину прямоугольника: "))
symb = input("Введите символ: ")

spaces = " " * (weignt - 2)

print(symb * (weignt + 2))
for i in range(height - 2):
    print(symb, spaces, symb)
print(symb * (weignt + 2))