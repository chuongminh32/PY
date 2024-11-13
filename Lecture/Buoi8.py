# # # * numpy lib 
# # ETL : trich xuat, chuyen doi 
# # - data store : data warehouse, data lake, 
# # - data process : tap trung, phan tan, theo lo, theo time
# # - lam sach: trung, ko nhat quan, du thua , dinh dang sai   
# # - cac loai phan tich: mo ta, chuan doan, du doan, de xuat.
# # - ky thuat phan tich data: cum, theo nhom, hoi quy, nhan to, data, van ban, chuoi time, cay quyet dinh, thuoc tinh
# 1. Tạo ma trận cơ bản:
# Ma trận toàn 0: np.zeros((row, col))
# Ma trận toàn 1: np.ones((row, col))
# Phát sinh các phần tử theo dải số: np.arange(start, stop, size = (row, col))
# Ma trận toàn giá trị cụ thể: np.full((row, col), value)
# Ma trận ngẫu nhiên: np.random.randn(row, col)
# Ma trận đơn vị (identity matrix): np.eye(size)
# Ma trận đường chéo: np.diag(arr)
# Giữ nguyên giá trị ngẫu nhiên với seed: np.random.seed(value)
# 2. Truy cập và thao tác với ma trận:
# Chọn phần tử cụ thể: matrix[row, col]
# Chọn sub-matrix: matrix[start_row:end_row, start_col:end_col]
# Chuyển vị (transpose): np.transpose(matrix)
# Thay đổi kích thước ma trận (reshape): np.reshape(matrix, (new_row, new_col))
# 3. Ghép và tách ma trận:
# Ghép theo chiều dọc (hàng): np.concatenate((matrix1, matrix2), axis=0)
# Ghép theo chiều ngang (cột): np.concatenate((matrix1, matrix2), axis=1)
# Ghép theo chiều sâu (3D): np.dstack((matrix1, matrix2))
# Tách ma trận: np.split(matrix, num_parts, axis)
# 4. Các phép toán ma trận:
# Cộng, trừ ma trận: matrix1 + matrix2, matrix1 - matrix2
# Nhân từng phần tử: matrix1 * matrix2
# Nhân ma trận: np.dot(matrix1, matrix2)
# Ma trận nghịch đảo: np.linalg.inv(matrix)
# Phần tử lớn nhất/nhỏ nhất: np.max(matrix), np.min(matrix)
# Tìm chỉ số phần tử lớn nhất: np.argmax(matrix)
# Sắp xếp ma trận: np.argsort(matrix, axis=0 hoặc axis=1)
# 5. Phép toán nâng cao:
# Phát sinh mảng ngẫu nhiên: np.random.randint(low, high, size)
# Mở rộng ma trận thành 3 chiều: np.expand_dims(matrix, axis)
# Chọn phần tử theo điều kiện: np.where(condition)

# import numpy as np
# import random

# # 1. Tạo ma trận toàn 0
# zero_matrix = np.zeros((3, 4))  # Ma trận 3 hàng, 4 cột toàn 0
# print("Ma trận toàn 0:\n", zero_matrix)

# # 2. Tạo ma trận toàn 1
# one_matrix = np.ones((3, 4))  # Ma trận 3 hàng, 4 cột toàn 1
# print("\nMa trận toàn 1:\n", one_matrix)

# # 3. Phát sinh các phần tử từ 1 đến 9 (dải số)
# arr = np.arange(1, 10)
# print("\nPhát sinh các phần tử từ 1 đến 9:\n", arr)

# # 4. Tạo ma trận toàn giá trị cụ thể (ví dụ: toàn số 7)
# full_matrix = np.full((3, 4), 7)  # Ma trận 3x4 toàn giá trị 7
# print("\nMa trận toàn giá trị 7:\n", full_matrix)

# # 5. Tạo ma trận ngẫu nhiên với phân phối chuẩn
# random_matrix = np.random.randn(3, 3)  # Ma trận 3x3 với các phần tử ngẫu nhiên
# print("\nMa trận ngẫu nhiên (phân phối chuẩn):\n", random_matrix)

# # 6. Tạo ma trận vuông đơn vị
# identity_matrix = np.eye(3)  # Ma trận đơn vị 3x3
# print("\nMa trận đơn vị 3x3:\n", identity_matrix)

# # 7. Tạo ma trận đường chéo từ một mảng
# diagonal_matrix = np.diag(arr[:3])  # Tạo ma trận đường chéo từ các phần tử đầu tiên của arr
# print("\nMa trận đường chéo từ mảng [1, 2, 3]:\n", diagonal_matrix)

# # 8. Giữ nguyên giá trị ngẫu nhiên ban đầu (np.random.seed)
# np.random.seed(2)  # Đặt seed để giá trị ngẫu nhiên cố định
# fixed_random_matrix = np.random.randn(3, 3)
# print("\nMa trận ngẫu nhiên với seed cố định:\n", fixed_random_matrix)

# # 9. Thao tác trên ma trận
# A = np.array([[1, 3, 6], [2, 7, 9]])
# B = np.array([[0, 4, 5], [1, 6, 10]])

# # Tìm phần tử nhỏ nhất trong toàn bộ ma trận A
# min_A = np.min(A)
# print("\nPhần tử nhỏ nhất trong ma trận A:", min_A)

# # Tìm phần tử nhỏ nhất theo từng dòng của ma trận A
# min_A_rows = np.amin(A, axis=1)
# print("Phần tử nhỏ nhất theo từng dòng của ma trận A:", min_A_rows)

# # Tìm phần tử nhỏ nhất theo từng cột của ma trận A
# min_A_cols = np.amin(A, axis=0)
# print("Phần tử nhỏ nhất theo từng cột của ma trận A:", min_A_cols)

# # Ghép hai ma trận
# concatenated = np.concatenate((A, B), axis=0)  # Ghép theo chiều dọc
# print("\nGhép hai ma trận theo chiều dọc:\n", concatenated)

# # Chuyển vị ma trận
# transposed = np.transpose(A)  # Chuyển vị ma trận A
# print("\nChuyển vị của ma trận A:\n", transposed)

# # Đổi kích thước ma trận
# reshaped = np.reshape(A, (3, 2))  # Đổi kích thước thành 3x2
# print("\nĐổi kích thước của ma trận A thành 3x2:\n", reshaped)

# # Tìm phần tử lớn nhất trong A và B
# max_elements = np.maximum(A, B)  # Tìm phần tử lớn nhất ở cùng vị trí
# print("\nPhần tử lớn nhất ở cùng vị trí giữa A và B:\n", max_elements)

# # Tách ma trận đã ghép thành 2 phần
# arr1, arr2 = np.split(concatenated, 2, axis=0)
# print("\nTách ma trận đã ghép:\n", arr1)
# print(arr2)





# X[1:3, 1:3] : dong 1 -> 2, cot 1 -> 2 
# # X[ [0, 2], : ] : dong 0, 2, lay tat ca cac cot 

# # x = np.array([[1, 2, 3, 4],
# #              [4, 5, 6, 2],
# #              [7, 8, 9, 1],
# #              [2, 5, 1, 5]] )

# # X = [[1, 2, 3, 4],
# #     [4, 5, 6, 2],]
# # Y = [ [7, 8, 9, 1],
# #     [2, 5, 1, 5],]
            
# # print(x[1, 2]) # x[1][2]
# # print(x[1:3, 1:3]) # row 1-> 2, col 1->2
# # print(x[:2, :2]) # truy cap 2 row, col dau tien 
# # print(x[-2:, -2:]) # truy cap 2 rol, col cuoi 
# # print(x[[0, 2], :]) # truy cap dong 0 va 2, lay tat ca cac cot 

# # print(x[0:2, 1:3])
# # print(x[0:3, [0,2]]) # row 0-> 2, col 0, col 2
# # print(np.diag(x))
# # print(x[0:2, [0,3]])
# # print(x[0:4, 1:3])