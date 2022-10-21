import numpy as np

size = int(input("Введите размерность квадратной матрицы 1 < N < 31 : "))
while (size < 1) or (size > 31):
    size = int(input("Вы ввели неверное число\nВведите размерность 1 < N < 31 : "))


matrix = np.random.randint(5, size=(size, size))
range_mat = np.linalg.matrix_rank(matrix)

print("Матрица:\n", matrix)
print("Ранг матрицы:", range_mat)


t = int(input('Введите количество знаков после запятой: '))
t = 0.1**t

factorial = 1
n = 1
summ = 0
new_summ = 0
drob = 1
while abs(drob) > t:
    new_summ += summ
    summ += (np.linalg.det(np.linalg.matrix_power(matrix, 2*n))) / factorial
    n += 1
    factorial = factorial * (2*n) * (2*n - 1)
    drob = new_summ - summ
    new_summ = 0
    print(n - 1, ':', summ, ' ', drob)

print('Сумма знакопеременного ряда:', summ)
