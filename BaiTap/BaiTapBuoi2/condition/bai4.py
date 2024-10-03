# import math

# def solveQuadraticEquation(a, b, c):
#     if a == 0:
#         if b == 0:
#             if c == 0:
#                 return "Phương trình vô số nghiệm"
#             else:
#                 return "Phương trình vô nghiệm"
#         else:
#             return f"x = {-c/b:.2f}"
#     else:
#         delta = b**2 - 4*a*c
#         if delta < 0:
#             return "Phương trình vô nghiệm"
#         elif delta == 0:
#             return f"Phương trình có nghiệm kép: x = {-b/(2*a):.2f}"
#         else:
#             x1 = (-b + math.sqrt(delta)) / (2*a)
#             x2 = (-b - math.sqrt(delta)) / (2*a)
#             return f"Phương trình có 2 nghiệm: x1 = {x1:.2f}, x2 = {x2:.2f}"

# # Ví dụ sử dụng hàm
# result = solveQuadraticEquation(1, 5, 2)
# print(result)
