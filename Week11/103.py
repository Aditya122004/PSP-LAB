import numpy as np
import time
import random

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took: {end - start:.6f} seconds")
        return result
    return wrapper


@timer
def custom_add(A, B):
    rows, cols = len(A), len(A[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    return result


@timer
def custom_sub(A, B):
    rows, cols = len(A), len(A[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] - B[i][j]
    return result


@timer
def custom_mul(A, B):
    rowsA, colsA = len(A), len(A[0])
    rowsB, colsB = len(B), len(B[0])
    result = [[0] * colsB for _ in range(rowsA)]

    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                result[i][j] += A[i][k] * B[k][j]
    return result


@timer
def numpy_add(A, B):
    return A + B

@timer
def numpy_sub(A, B):
    return A - B

@timer
def numpy_mul(A, B):
    return A @ B

size = 200
A = [[random.randint(1, 10) for i in range(size)] for j in range(size)]
B = [[random.randint(1, 10) for i in range(size)] for j in range(size)]
A_np = np.array(A)
B_np = np.array(B)

print("Custom Functions:")
custom_add(A, B)
custom_sub(A, B)
custom_mul(A, B)

print("NumPy Functions:")
numpy_add(A_np, B_np)
numpy_sub(A_np, B_np)
numpy_mul(A_np, B_np)
