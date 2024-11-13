import numpy as np

def product(mat_a, mat_b):
    try:
        # Tích ma trận thông thường
        mat_product = np.dot(mat_a, mat_b)
        print("Tích ma trận:")
        print(mat_product)
    except ValueError:
        print("Không có tích ma trận")
        
    try:
        # Tích Hadamard
        hadamard_product = mat_a * mat_b
        print("Tích Hadamard:")
        print(hadamard_product)
    except ValueError:
        print("Không có tích Hadamard")

# Ví dụ sử dụng
if __name__ == "__main__":
    mat_a = np.array([[1, 2], [3, 4]])
    mat_b = np.array([[5, 6], [7, 8]])
    product(mat_a, mat_b)
