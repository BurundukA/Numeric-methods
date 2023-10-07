import numpy as np

def lu_decomposition(A):
    n = A.shape[0]
    L = np.zeros_like(A, dtype=float)
    U = np.zeros_like(A, dtype=float)

    for i in range(n):
        L[i, i] = 1.0

        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])

        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]

    return L, U

def solve_lu(A, b):
    L, U = lu_decomposition(A)

    n = A.shape[0]
    y = np.zeros(n, dtype=float)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    x = np.zeros(n, dtype=float)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x

# Example usage:
A = np.array([[2, 1, -1],
              [1, 3, 2],
              [3, 2, -3]], dtype=float)
b = np.array([8, 10, 18], dtype=float)

solution = solve_lu(A, b)
print("Solution:", solution)
