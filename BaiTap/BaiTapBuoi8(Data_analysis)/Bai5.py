import numpy as np

def create_evenly_spaced_array(a, b):
    # Tạo mảng chứa 20 số thực cách đều nhau từ a đến b
    return np.linspace(a, b, num=20)

if __name__ == "__main__":
    try:
        a = float(input("Nhập a: "))  # Nhập giá trị a từ người dùng
        b = float(input("Nhập b: "))  # Nhập giá trị b từ người dùng
        
        if a < b:  # Kiểm tra xem a có nhỏ hơn b không
            array = create_evenly_spaced_array(a, b)
            print("Mảng chứa 20 số thực cách đều nhau thuộc khoảng (a, b):", array)
        else:
            print("Vui lòng đảm bảo a < b.")
    except ValueError:
        print("Vui lòng nhập các giá trị hợp lệ cho a và b.")
