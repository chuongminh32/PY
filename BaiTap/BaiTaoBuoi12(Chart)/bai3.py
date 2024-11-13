import matplotlib.pyplot as plt

# Dữ liệu
categories = ['A', 'B', 'C', 'D', 'E']  # Các nhóm
values = [23, 45, 56, 78, 33]  # Giá trị của các nhóm

# Vẽ biểu đồ cột
plt.bar(categories, values, color='skyblue')

# Thêm tiêu đề và nhãn cho trục
plt.title('Biểu đồ cột minh họa')
plt.xlabel('Nhóm')
plt.ylabel('Giá trị')

# Hiển thị biểu đồ
plt.show()
