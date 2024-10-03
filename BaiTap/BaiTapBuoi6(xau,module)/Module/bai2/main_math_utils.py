# main_math_utils.py
from math_utils.quadratic_solver import solve_quadratic
from math_utils.sort_ascending import sort_ascending
from math_utils.sort_descending import sort_descending

def main():
    # Tìm nghiệm phương trình bậc 2
    print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    roots = solve_quadratic(a, b, c)
    print(f"Nghiệm của phương trình là: {roots}")

    # Sắp xếp mảng tăng dần
    arr = [int(x) for x in input("Nhập mảng số (cách nhau bằng dấu cách): ").split()]
    sorted_arr_asc = sort_ascending(arr)
    print("Mảng đã sắp xếp tăng dần:", sorted_arr_asc)

    # Sắp xếp mảng giảm dần
    sorted_arr_desc = sort_descending(arr)
    print("Mảng đã sắp xếp giảm dần:", sorted_arr_desc)

if __name__ == "__main__":
    main()
