import numpy as np

def jacobi_eigenvalue(A, tol=1e-9, max_iter=1000):
    n = A.shape[0]
    eigenvalues = np.zeros(n)
    eigenvectors = np.identity(n)
    for _ in range(max_iter):
        maxval = 0
        p, q = 0, 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i, j]) > maxval:
                    maxval = abs(A[i, j])
                    p, q = i, j
        if maxval < tol:
            break
        theta = 0.5 * np.arctan2(2 * A[p, q], A[q, q] - A[p, p])
        c = np.cos(theta)
        s = np.sin(theta)
        R = np.identity(n)
        R[p, p] = c
        R[q, q] = c
        R[p, q] = -s
        R[q, p] = s
        A = np.dot(np.dot(R.T, A), R)
        eigenvectors = np.dot(eigenvectors, R)
    eigenvalues = np.diag(A)
    return eigenvalues, eigenvectors

# Simple example
if __name__ == "__main__":
    A = np.array([[4, -2, 2],
                 [-2, 3, -1],
                 [2, -1, 3]])

    eigenvalues, eigenvectors = jacobi_eigenvalue(A)

    print("Eigenvalues:")
    print(eigenvalues)
    print("Eigenvectors:")
    print(eigenvectors)
