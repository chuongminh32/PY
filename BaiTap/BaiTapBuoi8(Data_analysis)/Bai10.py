# isinstance(object, classinfo)
import numpy as np

def transpose(mat):
    # Kiểm tra xem mat có phải là một numpy array không
    if not isinstance(mat, np.ndarray):
        raise ValueError("mat must be a numpy array")
    
    # Kiểm tra xem mat có phải là ma trận 2D không
    if mat.ndim != 2:
        raise ValueError("mat must be a 2D array")
    
    # Tính toán ma trận chuyển vị
    return np.transpose(mat)

if __name__ == "__main__":
    # Ví dụ sử dụng
    mat = np.array([[1, 2], 
                    [3, 4], 
                    [5, 6]])
    
    result = transpose(mat)
    print("Ma trận ban đầu:")
    print(mat)
    print("Ma trận chuyển vị:")
    print(result)
