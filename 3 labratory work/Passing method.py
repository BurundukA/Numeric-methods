import numpy as np

def sor_method(A, b, omega, tol=1e-6, max_iter=1000):
    n = len(b)
    x = np.zeros(n)

    for k in range(max_iter):
        for i in range(n):
            x[i] = (1 - omega) * x[i] + (omega / A[i, i]) * (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x[i + 1:]))

        if np.linalg.norm(np.dot(A, x) - b) < tol:
            return x

    raise ValueError("SOR Method did not converge within the specified number of iterations.")

# Example usage:
A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 3]], dtype=float)
b = np.array([3, 5, -1], dtype=float)

omega = 1.25

solution = sor_method(A, b, omega)
print("Solution:", solution)
