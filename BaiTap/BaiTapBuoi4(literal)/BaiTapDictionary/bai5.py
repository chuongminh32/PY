# infoStudent = {}

# n = int(input("Nhap so luong sinh vien: "))

# for i in range(n):
#     print(f"Nhap thong tin sinh vien thu {i+1}:")
#     name = (input("Nhap ten: "))
#     score = int(input("Nhap diem [0-10]: "))
#     while 1:
#         if score < 0 or score > 10:
#             score = int(input("Loi, Nhap diem [0-10]: "))
#         else:
#             break

#     infoStudent[name] = score
# print("Thong tin sinh vien:")
# print(infoStudent)


# # khoi tao dict voi key = [0-10], value = list rong
# # rankScore = {}
# # for i in range(11):
#     # rankScore[i] = []

# # sortsyntax
# rankScore = {i: [] for i in range(11)}

# # value = score, key = name
# for key, value in infoStudent.items():
#     rankScore[value].append(key)

# print("Danh sách sinh viên theo điểm:")
# print(rankScore)
