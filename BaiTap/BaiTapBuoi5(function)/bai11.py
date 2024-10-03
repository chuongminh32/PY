# import math

# def solve_quadratic(a, b, c):
#     if a == 0:
#         return []  # Không phải phương trình bậc hai
#     delta = b**2 - 4*a*c
#     if delta < 0:
#         return []  # Vô nghiệm
#     elif delta == 0:
#         x = -b / (2 * a)
#         return [x]  # Có nghiệm kép
#     else:
#         x1 = (-b + math.sqrt(delta)) / (2 * a)
#         x2 = (-b - math.sqrt(delta)) / (2 * a)
#         return [x1, x2]  # Hai nghiệm phân biệt

# # Ví dụ sử dụng
# print(solve_quadratic(1, -3, 2))  # [2.0, 1.0]
