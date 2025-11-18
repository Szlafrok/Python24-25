import numpy as np

def is_symmetric(matrix: np.ndarray) -> bool:
    if matrix.shape[0] != matrix.shape[1]:
        return False

    return np.array_equal(matrix, matrix.transpose())

matrix = np.array([[1, 2, 3],
                   [2, 5, 6],
                   [3, 6, 9]])
print(is_symmetric(matrix))
print(matrix.shape)

# Super rozwiązanie i dobry warunek początkowy w funkcji!

# 3 / 3