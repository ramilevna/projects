import sys

matrix1 = []
matrix2 = []
print("Сколько строк в матрице?")
n = int(input())
print("Сколько столбцов в матрице?")
m = int(input())
for i in range(n):
    print(f"Введите {i + 1} строку.")
    list = input().split()
    if len(list) != m:
        print("Ошибка ввода")
        sys.exit(0)
    for j in range(len(list)):
        list[j] = int(list[j])
    matrix1.append(list)
    list = []
print("Первая матрица:")
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        print(matrix1[i][j], end=" ")
    print()
for i in range(n):
    print(f"Введите {i + 1} строку.")
    list = input().split()
    if len(list) != m:
        print("Ошибка ввода")
        sys.exit(0)
    for j in range(len(list)):
        list[j] = int(list[j])
    matrix2.append(list)
    list = []
print("Вторая матрица:")
for i in range(len(matrix2)):
    for j in range(len(matrix2[i])):
        print(matrix2[i][j], end=" ")
    print()
print("Выберете операция: +/-")
symb = input()
if symb != "+" and symb != "-":
    sys.exit(0)
elif symb == "+":
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix1[i][j] += matrix2[i][j]
else:
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix1[i][j] -= matrix2[i][j]
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        print(matrix1[i][j], end=" ")
    print()