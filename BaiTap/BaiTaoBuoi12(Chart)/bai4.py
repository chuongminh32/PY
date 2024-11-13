import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu ngẫu nhiên từ phân phối chuẩn (mean=0, std=1)
data = np.random.randn(1000)

# Vẽ histogram
plt.hist(data, bins=30, color='skyblue', alpha=0.7, edgecolor='black')

# Thêm tiêu đề và nhãn cho các trục
plt.title('Histogram của dữ liệu phân phối chuẩn')
plt.xlabel('Giá trị')
plt.ylabel('Tần suất')

# Hiển thị biểu đồ
plt.show()
