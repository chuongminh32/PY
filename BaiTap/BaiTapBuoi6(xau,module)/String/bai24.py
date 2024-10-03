# def solve(s):
#     s = s.lower()
#     dict_str = {}
#     lst = s.split(' ')
#     set_word = set(lst)
#     for word in set_word:
#         dict_str[word] = lst.count(word)
#     return dict_str

# s = input("s: ")
# print(solve(s))

# c2 
# def count_words(s):
#     # Chuyển chuỗi về chữ thường
#     s = s.lower()

#     # Tách các từ dựa trên khoảng trắng
#     words = s.split()

#     # Tạo từ điển để đếm số lần xuất hiện của mỗi từ
#     word_count = {}

#     # Đếm từ
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1

#     return word_count

# # Test chương trình
# s = input("Nhập chuỗi: ")
# result = count_words(s)

# # In kết quả
# for word, count in result.items():
#     print(f"Từ '{word}' xuất hiện {count} lần.")
