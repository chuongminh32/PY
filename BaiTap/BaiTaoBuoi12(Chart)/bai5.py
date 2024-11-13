import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Tạo lưới x, y
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
x, y = np.meshgrid(x, y)

# Tính giá trị của z theo phương trình đã biến đổi
z_positive = np.sqrt(0.3 * x**2 + 0.3 * y**2 + 1)  # Nhánh dương
z_negative = -np.sqrt(0.3 * x**2 + 0.3 * y**2 + 1)  # Nhánh âm

# Vẽ biểu đồ 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Vẽ mặt trên (z dương)
surf_positive = ax.plot_surface(x, y, z_positive, cmap='jet', vmin=-5, vmax=5)

# Vẽ mặt dưới (z âm)
surf_negative = ax.plot_surface(x, y, z_negative, cmap='jet', vmin=-5, vmax=5)

# Thêm tiêu đề và nhãn
ax.set_title('3D Hyperboloid: $-0.3x^2 - 0.3y^2 + z^2 = 1$', fontsize=14)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Hiển thị thanh màu (colorbar)
fig.colorbar(surf_positive, ax=ax, shrink=0.5, aspect=5)

# Hiển thị đồ thị
plt.show()
