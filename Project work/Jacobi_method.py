import numpy as np

def jacobi_method(A, b, epsilon=1e-6, max_iterations=1000):
    n = len(b)

    # Устанваить начальне приближение
    x = np.zeros(n)

    for k in range(max_iterations):
        x_old = x.copy()

        # Считаем следующе приближение
        for i in range(n):
            sigma = np.dot(A[i, :], x_old) - A[i, i] * x_old[i]
            x[i] = x_old[i] + (b[i] - sigma) / A[i, i]

        # Проверка на приближение
        if np.linalg.norm(A @ x - b, np.inf) < epsilon:
            return x

    print("Достигнуто максимально допсутимео кол-во итераций!")
    return x