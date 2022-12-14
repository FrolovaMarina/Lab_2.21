import numpy as np
import math
from random import randint
import time
try:
    N = randint(1, 100)
    K = int(input("Введите ранг матрицы = "))
    count = int(input("Введите количество слагаемых = "))
    t = int(input("Введите точность вычислений = "))
    while K <= 0 or count <= 0 or t <= 0:
        if K <= 0:
            print("Число K не может являться рангом матрицы. Пожалуйста, введите K ещё раз.")
            K = int(input("Введите ранг матрицы = "))
        elif count <= 0:
            print("Число count не может являться количеством слагаемых. Пожалуйста, введите count ещё раз.")
            count = int(input("Введите количество слагаемых = "))
        elif t <= 0:
            print("Число K не может являться точностью вычислений. Пожалуйста, введите t ещё раз.")
            t = int(input("Введите точность вычислений = "))
    A = np.random.randint(-10, 10, (N, N))
    rank = np.linalg.matrix_rank(A)
    res = 0
    while rank != K:
        N = randint(1, 100)
        A = np.random.randint(-10, 10, (N, N))
        rank = np.linalg.matrix_rank(A)
    print("A = ")
    print(A)
    start = time.time()
    x = A.view()
    res = 0
    for n in range(1, count + 1):
        x = 2 * A * math.factorial(n)
        print("x = ")
        print(x)
        det = int(np.linalg.det(x))
        res = det / math.factorial(2*n) + res
        res = round(res, t)
        print("res =", res)
    res = round(res, t)
    print("Результат работы программы =", res)
    finish = time.time()
    result = finish - start
    print("Время выполнения программы: " + str(result) + " секунд.")
except ValueError:
    print("Это не число")
