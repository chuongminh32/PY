import numpy as np

def create_random_array(a, b):
    # Tạo mảng chứa 10 số thực ngẫu nhiên trong khoảng (a, b)
    return a + (b - a) * np.random.rand(10)

if __name__ == "__main__":
    try:
        a = float(input("Nhập a: "))  # Nhập giá trị a từ người dùng
        b = float(input("Nhập b: "))  # Nhập giá trị b từ người dùng
        
        if a < b:  # Kiểm tra xem a có nhỏ hơn b không
            array = create_random_array(a, b)
            print("Mảng chứa 10 số thực ngẫu nhiên trong khoảng (a, b):", array)
        else:
            print("Vui lòng đảm bảo a < b.")
    except ValueError:
        print("Vui lòng nhập các giá trị hợp lệ cho a và b.")
