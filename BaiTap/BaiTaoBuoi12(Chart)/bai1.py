import numpy as np
from matplotlib import pyplot as plt

# Tạo giá trị x từ -6 đến 4, với bước nhảy 0.1
x = np.arange(-6, 4, 0.1)

# Tính giá trị y dựa trên phương trình đa thức
y =  3 * x**5 + 20 * x**4 - 10 * x**3 - 240 * x**2 - 250 * x + 200

# size 
plt.figure(figsize=(8, 6))

# Vẽ đồ thị với đường chấm đỏ (r--) và độ dày đường là 3
plt.plot(x, y, 'r-.', linewidth=3)
# plt.plot(x, y, 'r--', linewidth=3, label=r"$y = 3x^5 + 20x^4 - 10x^3 - 240x^2 - 250x + 200$")

# Thêm tiêu đề cho đồ thị
plt.title("Fifth Degree Polynomial")


# Thêm nhãn cho trục x và y
plt.xlabel("x", fontsize=12)  # Nhãn cho trục x với cỡ chữ 12
plt.ylabel("y", fontsize=12)  # Nhãn cho trục y với cỡ chữ 12

# Cài đặt giới hạn cho trục x và y
plt.xlim(-6, 4)  # Giới hạn trục x từ -6 đến 4
plt.ylim(-1200, 400)  # Giới hạn trục y từ -1200 đến 400


# Hiển thị đồ thị
plt.show()
