# def all_repeat_sub(s):
#     # Tập hợp để lưu trữ tất cả các xâu con khác nhau
#     sub = []

#     # Duyệt qua tất cả các chỉ số bắt đầu và kết thúc để tìm xâu con
#     for start in range(len(s)):
#         for end in range(start + 1, len(s) + 1):
#             # Lấy xâu con từ vị trí start đến end-1
#             substring = s[start:end]
#             sub.append(substring)
    
#     result = set()
#     for s in sub:
#         if sub.count(s) >=2:
#             result.add(s)
#     return result

# # Test chương trình
# input_str = input("Nhập vào một chuỗi: ")
# result = all_repeat_sub(input_str)
# print("Tất cả các xâu con lặp lại là:", result)
