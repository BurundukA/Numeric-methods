import numpy as np

def is_symmetric_positive_definite(A, b):
    # Проверка матрицы на симметричность
    if not np.allclose(A, A.T):
        print("Матрица не симметрична положительно определённа!")
        return

    # Проверка положительно определённости использованием собственных значений
    eigenvalues = np.linalg.eigvals(A)
    if np.all(eigenvalues > 0):
        solution = square_root_method(A, b)
        print("Solution:", solution)
        return True
    else:
        print("Матрица не симметрична положительно определённа!")
        return False

def cholesky_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))

    # Формирование матрицы U с помощью формул
    for i in range(n):
        for j in range(i + 1):
            if i == j:
                L[i, j] = np.sqrt(A[i, i] - np.sum(L[i, :j]**2))
            else:
                L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]

    return L

def square_root_method(A, b):
    L = cholesky_decomposition(A)

    # Прямой ход: Ly = b
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    # Обратный ход: L^Tx = y
    n = len(y)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(L.T[i, i + 1:], x[i + 1:])) / L.T[i, i]

    return x