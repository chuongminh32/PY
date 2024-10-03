# def cos_taylor(x, terms=100):
#     cos_x = 0
#     factorial = 1
#     for n in range(terms):
#         if n > 0:
#             factorial *= (2 * n) * (2 * n - 1)  # Tính giai thừa cho số hạng tiếp theo
#         cos_x += ((-1) ** n) * (x ** (2 * n)) / factorial
#     return cos_x

# # Ví dụ sử dụng
# print(cos_taylor(0))  # 1.0
