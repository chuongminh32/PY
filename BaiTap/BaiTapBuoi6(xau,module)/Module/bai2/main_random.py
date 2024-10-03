# main_random.py
from random_array import generate_random_array

def main():
    n = int(input("Nhập số lượng phần tử: "))
    min_value = int(input("Nhập giá trị tối thiểu: "))
    max_value = int(input("Nhập giá trị tối đa: "))
    
    random_array = generate_random_array(n, min_value, max_value)
    print("Dãy số ngẫu nhiên:", random_array)

if __name__ == "__main__":
    main()
