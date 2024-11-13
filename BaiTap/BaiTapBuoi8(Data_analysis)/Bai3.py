import numpy as np

# Bước 1: Tạo mảng một chiều với các giá trị ngẫu nhiên
np.random.seed(0)  # Đặt seed để có kết quả lặp lại
random_array = np.random.randint(0, 100, size=10)  # Tạo mảng với 10 giá trị nguyên ngẫu nhiên từ 0 đến 99
print("Mảng ngẫu nhiên:\n", random_array)

# Bước 2: Tìm chỉ mục của số lớn nhất
index_of_max = np.argmax(random_array)  # Tìm chỉ mục của số lớn nhất
print("Chỉ mục của số lớn nhất:", index_of_max)
print("Giá trị lớn nhất:", random_array[index_of_max])

