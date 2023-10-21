import numpy as np

def power_iteration(matrix, num_iterations, initial_vector=None):
    n = matrix.shape[0]
    if initial_vector is None:
        initial_vector = np.random.rand(n)
    b = initial_vector
    for i in range(num_iterations):
        b = np.dot(matrix, b)
        # Normalization
        norm = np.linalg.norm(b)
        b = b / norm
    eigenvalue = np.dot(np.dot(b, matrix), b)
    return eigenvalue, b

#Small example
if __name__ == "__main__":
    A = np.array([[2, -1, 0],
                 [-1, 2, -1],
                 [0, -1, 2]])
    num_iterations = 1000
    initial_vector = np.random.rand(3)
    max_eigenvalue, max_eigenvector = power_iteration(A, num_iterations, initial_vector)
    print("Matrix A:")
    print(A)
    print("Initial Vector b:")
    print(initial_vector)
    print("Maximum Modulus Eigenvalue:", max_eigenvalue)
    print("Corresponding Eigenvector:", max_eigenvector)
