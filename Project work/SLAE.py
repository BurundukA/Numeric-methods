import numpy as np
import math
import copy

def choice_of_method(A,b):
    #Если уравнений болье 100, тоитерационный мтеод

    A1 = np.asarray(A)
    n, m = A1.shape

    #Если кол-во уравнений меньше 100, то импользовать олине
    if n<=100:
        matrix = np.array(A)
        n1 = matrix.shape[0]

        if n != m:
            print("Матрица некорректного размера!")

        # Проверка матрицы на тридиагональность
        for i in range(n):
            for j in range(i + 2, n):
                if A1[i, j] != 0:
                    # Проверка на наличие угловых миноров
                    for k in range(1, n1):
                        submatrix = matrix[:k, :k]
                        determinant = np.linalg.det(submatrix)
                        if determinant == 0:
                            solution = gaussian_elimination_pivoting(A, b)
                            print("Решение было получено методом Гаусса", solution)
                            return solution
                    solution = lu_decomposition_and_solve(A, b)
                    print("Решение было получено методом LU-разложения", solution)
                    return solution
        solution = thomas_algorithm(A, b)
        print("Решение было получено методом прогонки:", solution)
        return solution
    else:
        matrix = np.array(A)
        n1 = matrix.shape[0]
        # Проверка на наличие угловых миноров
        for k in range(1, n1):
            submatrix = matrix[:k, :k]
            determinant = np.linalg.det(submatrix)
            if determinant == 0:
                solution = simple_iterations(A, b)
                print("Решение было получено методом простых итераций", solution)
                return solution
        solution = seidel_method(A, b)
        print("Решение было получено методом Зейделя", solution)
        return solution


def check_correctness(A,b):
    solution = choice_of_method(A,b)
    n = len(b)
    for i in range(n):
        solution_k =0
        #Вычисляем значения уравнений
        for j in range(n):
            solution_k += A[i][j]*solution[j]
        #Сравниванием полученное значение со свобоным членом
        if(solution_k != b[i]):
            print("Решение неверно!")
            return
        print("Решение верно!")
        return

def gaussian_elimination_pivoting(A, b):
    A = A.astype(np.float64)
    b = b.astype(np.float64)

    n = len(b)

    # Создание дополненной матрицы (A|b)
    augmented_matrix = np.column_stack((A, b))

    for i in range(n):
        # Поиск ведущего элемента, перемещение строк
        max_row = i + np.argmax(np.abs(augmented_matrix[i:, i]))
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]

        # Нормализация ведущего элемента (приведение к 1)
        leading_element = augmented_matrix[i, i]
        augmented_matrix[i, i:] /= leading_element

        # Прямой ход (создание верхнетреугольной матрицы)
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i]
            augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]

    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:n], x[i+1:])

    return x


def thomas_algorithm(A, b):

    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)

    n = len(b)

    under_diag = A.diagonal(offset=-1)
    main_diag = A.diagonal(offset=0)
    above_diag = A.diagonal(offset=1)

    p_prime = np.zeros(n - 1)
    q_prime = np.zeros(n)

    # Прямой ход
    p_prime[0] = above_diag[0] / (-main_diag[0])
    q_prime[0] = (-b[0]) / (-main_diag[0])

    for i in range(1, n - 1):
        m = 1.0 / (-main_diag[i] - under_diag[i - 1] * p_prime[i - 1])
        p_prime[i] = above_diag[i] * m
        q_prime[i] = (-b[i] + under_diag[i - 1] * q_prime[i - 1]) * m

    # Обратный ход
    x = np.zeros(n)
    x[-1] = (-b[-1] + under_diag[-1] * q_prime[-2]) / (-main_diag[-1] - under_diag[-1] * p_prime[-1])

    for i in range(n - 2, -1, -1):
        x[i] = q_prime[i] + p_prime[i] * x[i + 1]

    return x


def lu_decomposition_and_solve(A, b):
    n = len(b)

    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    # LU- разложение
    for i in range(n):
        # Составление матрицы U
        for k in range(i, n):
            sum_ = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_

        # Составление матрицы L
        for k in range(i, n):
            if i == k:
                L[i][i] = 1.0
            else:
                sum_ = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - sum_) / U[i][i]

    # Решение Ly = b обратных ходом
    y = [0.0] * n
    for i in range(n):
        sum_ = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_) / L[i][i]

    # Решение Ux = y обратных ходом
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        sum_ = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - sum_) / U[i][i]

    return x


def simple_iterations(A, b, initial_guess = np.array([0, 0, 0]), epsilon = 1e-6, max_iterations=1000):
    n = len(b)

    # Привести систему к виду x = αx + β
    alpha = np.linalg.inv(A)
    beta = np.dot(alpha, b)

    # Установить начальное приближение
    x_k = initial_guess

    for k in range(max_iterations):
        # Считаем следующе приближение используя формулу x(k+1) = αx(k) + β
        x_k1 = np.dot(alpha, x_k) + beta

        # Проверка на приближение
        if np.linalg.norm(x_k1 - x_k) < epsilon:
            return x_k1

        x_k = x_k1

    print("Достигнуто максимально допсутимео кол-во итераций!")
    return x_k

def seidel_method(A, b, initial_guess=None, epsilon=1e-8, max_iterations=1000):
    n = len(b)
    #LU-разложение матрицы
    L = np.tril(A, k=-1)
    U = np.triu(A, k=1)
    D_inv = np.linalg.inv(np.diag(np.diag(A)))

    #Устанваить начальне приближение
    x_k = np.zeros(n) if initial_guess is None else initial_guess.copy()

    for k in range(max_iterations):
        # Считаем следующе приближение
        x_k1 = np.dot(D_inv, b - np.dot((L + U), x_k))

        # Проверка на приближение
        if np.linalg.norm(x_k1 - x_k) < epsilon:
            return x_k1

        x_k = x_k1.copy()

    print("Достигнуто максимально допсутимео кол-во итераций!")
    return x_k
