import numpy as np

def broadcast(vec, n):
    # Kiểm tra xem vec có phải là một numpy array không
    if not isinstance(vec, np.ndarray):
        raise ValueError("vec must be a numpy array")
    
    # Đảm bảo rằng vec là một vector 1D
    if vec.ndim != 1:
        raise ValueError("vec must be a 1D array")
    
    # Tạo ma trận mới bằng cách lặp lại vec n lần theo chiều cột
    result = np.tile(vec[:, np.newaxis], (1, n))
    return result

if __name__ == "__main__":
    # Ví dụ sử dụng
    vec = np.array([6, 7, 4])  # Vector đầu vào
    n = 3  # Số cột cần tạo ra
    result = broadcast(vec, n)
    print("Kết quả broadcast:")
    print(result)
