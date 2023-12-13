import numpy as np

def qr_decomposition(A):
    m, n = A.shape
    Q = np.zeros((m, m))
    R = np.zeros((m, n))

    # QR-разложение
    for j in range(m):
        v = A[:, j].astype(float)
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v -= R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]

    return Q, R

def solve_with_qr(A, b):
    Q, R = qr_decomposition(A)

    # Решение Q^T * y = b прямым ходом
    y = np.dot(Q.T, b.astype(float))

    # Решение Rx = y обратным ходом
    n = len(b)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(R[i, i + 1:], x[i + 1:])) / R[i, i]

    return x