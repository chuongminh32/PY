# """.1 Hàm title()
# Công dụng: Hàm title() chuyển đổi chuỗi thành dạng tiêu đề (title case),
#  trong đó mỗi từ bắt đầu bằng chữ cái hoa, và các chữ cái còn lại là chữ cái thường.
#  Hàm này sẽ không thay đổi ký tự không phải là chữ cái."""


# """2. Hàm translate()""
# Công dụng: Hàm translate() sử dụng để thay thế các ký tự trong chuỗi theo bảng dịch 
# (translation table) được cung cấp.Để sử dụng hàm này, bạn cần tạo một bảng dịch bằng
#  cách sử dụng hàm str.maketrans()."""""

# #  Ex: 
# Tạo bảng dịch
# trans_table = str.maketrans("12345", "Hello")  # Thay thế a->1, e->2, i->3, o->4, u->5

# text = "12345 world! welcome to python programming."

# # Áp dụng hàm translate
# translated_text = text.translate(trans_table)
# print("Chuỗi đã dịch:", translated_text)  # Kết quả: "h2ll4 w4rld! w2lc4m2 t4 pyth4n pr4gr1mm3ng."

# # Áp dụng hàm title
# title_case = translated_text.title()
# print("Chuỗi tiêu đề:", title_case)  # Kết quả: "H2Ll4 W4Rld! W2Lc4M2 T4 Pyth4N Pr4Gr1Mm3Ng."
