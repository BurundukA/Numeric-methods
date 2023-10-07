import numpy as np

def elimination_method(A, b):
    n = len(b)

    augmented_matrix = np.hstack((A.astype(float), b.reshape(-1, 1).astype(float)))

    for i in range(n):
        max_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]

        pivot = augmented_matrix[i, i]
        augmented_matrix[i, :] /= pivot

        for j in range(i + 1, n):
            factor = augmented_matrix[j, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i, -1]
        for j in range(i + 1, n):
            x[i] -= augmented_matrix[i, j] * x[j]

    return x

# Example usage:
A = np.array([[2, 1, -1],
              [1, 3, 2],
              [3, 2, -3]], dtype=float)
b = np.array([8, 10, 18], dtype=float)

solution = elimination_method(A, b)
print("Solution:", solution)
