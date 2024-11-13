def replace_col(mat, col_ind):
    # Kiểm tra chỉ số cột có hợp lệ không
    if col_ind < 0 or col_ind >= mat.shape[1]:
        raise IndexError("Chỉ số cột không hợp lệ")

    # Thay thế toàn bộ giá trị trong cột thành 1
    # lay tat ca cac dong cua cot col_ind 
    mat[:, col_ind] = 1
    return mat

# Ví dụ sử dụng
if __name__ == "__main__":
    mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    col_ind = 1  # Thay thế cột thứ 1 (cột thứ 2)
    result = replace_col(mat, col_ind)
    print("Ma trận sau khi thay thế cột:")
    print(result)
