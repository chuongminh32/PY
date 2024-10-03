from math_utils.quadratic_solver import solve_quadratic
from math_utils.sort_ascending import sort_ascending
from math_utils.sort_descending import sort_descending

def main():
    # Sử dụng các hàm từ package math_utils
    print("Giải phương trình bậc 2:")
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    roots = solve_quadratic(a, b, c)
    print(f"Nghiệm của phương trình là: {roots}")

    arr = [int(x) for x in input("Nhập mảng số (cách nhau bằng dấu cách): ").split()]
    print("Mảng đã sắp xếp tăng dần:", sort_ascending(arr))
    print("Mảng đã sắp xếp giảm dần:", sort_descending(arr))

if __name__ == "__main__":
    main()
