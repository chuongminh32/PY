import numpy as np
import matplotlib.pyplot as plt

# Tạo giá trị cho x
x = np.arange(-3 * np.pi, 0, 0.1)
x2 = np.arange(0, 3 * np.pi, 0.1)
theta = np.linspace(-3 * np.pi, 3 * np.pi, 400)   

# Hàm y = 1.5 * sin(x)
y = 1.5 * np.sin(x)
r = 2 + np.cos(10 * theta) + 2 * np.sin(5 * theta)
y2 = 1.5 * np.sin(x2)


# Tạo figure cho đồ thị
plt.figure(figsize=(8, 6))

# Vẽ đồ thị 1  với đường màu đỏ 
plt.plot(x, y, 'r:', label=r"$y = 1.5\sin(x)$ with $x \in [-3\pi; 0]$", linewidth=3)

# Đồ thị thứ hai: r = 2 + cos(10θ) + 2sin(5θ)
plt.plot(theta, r, 'g-', label=r"$r = 2 + \cos(10\theta) + 2\sin(5\theta)$", linewidth=3)

# Vẽ đồ thị 2  với đường màu đỏ 
plt.plot(x2, y2, 'b:', label=r"$y = 1.5\sin(x)$ with $x \in [0; 3\pi]$", linewidth=3)

# Cài đặt giới hạn cho trục x và y
plt.xlim(-10, 10)  # Giới hạn trục x từ -10 đến 10
plt.ylim(-6, 6)  # Giới hạn trục y từ -6 đến 6

# Thêm grid
plt.grid(True)

# # Hiển thị legend
plt.legend()

# Hiển thị đồ thị
plt.show()

