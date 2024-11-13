import numpy as np

def create_odd_array(n):
    # Tạo mảng các số nguyên từ 1 đến N
    arr = np.arange(1, n + 1)
    # Lọc các số lẻ
    odd_numbers = arr[arr % 2 != 0]
    return odd_numbers

if __name__ == "__main__":
    n = int(input("Nhập N (số nguyên dương): "))  # Nhập số nguyên dương từ người dùng
    if n > 0:  # Kiểm tra xem N có phải là số dương không
        odd_array = create_odd_array(n)
        print("Mảng các số lẻ từ 1 đến N:", odd_array)
    else:
        print("Vui lòng nhập một số nguyên dương.")
