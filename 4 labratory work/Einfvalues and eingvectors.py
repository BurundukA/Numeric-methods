import numpy as np
from scipy.linalg import eig

# Example
A = np.array([[4, -2, 2],
             [-2, 3, -1],
             [2, -1, 3]])

eigenvalues, eigenvectors = eig(A)

print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
