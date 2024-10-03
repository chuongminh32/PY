# def solve(s):
#     unique_sub = set()
#     for start in range(len(s)):
#         for end in range(start+1, len(s)):
#             sub_str = s[start:end]
#             unique_sub.add(sub_str)

#     return unique_sub

# if __name__ == "__main__":
#     s = input("s: ")
#     print(solve(s))


# def all_unique_substrings(s):
#     # Tập hợp để lưu trữ tất cả các xâu con khác nhau
#     unique_substrings = set()

#     # Duyệt qua tất cả các chỉ số bắt đầu và kết thúc để tìm xâu con
#     for start in range(len(s)):
#         for end in range(start + 1, len(s) + 1):
#             # Lấy xâu con từ vị trí start đến end-1
#             substring = s[start:end]
#             unique_substrings.add(substring)

#     return unique_substrings

# # Test chương trình
# input_str = input("Nhập vào một chuỗi: ")
# result = all_unique_substrings(input_str)
# print("Tất cả các xâu con khác nhau là:")
# for substring in sorted(result):
#     print(substring)
