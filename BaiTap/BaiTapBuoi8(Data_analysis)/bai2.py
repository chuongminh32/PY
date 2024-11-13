import numpy as np

# Bước 1: Tạo mảng một chiều với các giá trị ngẫu nhiên
np.random.seed(0)  # Đặt seed để có kết quả lặp lại
random_array = np.random.randn(10) * 10  # Tạo mảng với 10 giá trị ngẫu nhiên từ phân phối chuẩn, nhân với 10
print("Mảng ngẫu nhiên ban đầu:\n", random_array)

# Bước 2: Lọc các giá trị số nguyên dương
positive_integers = random_array[random_array > 0].astype(int)  # Lọc và chuyển đổi sang kiểu int
print("\nMảng số nguyên dương:\n", positive_integers)
