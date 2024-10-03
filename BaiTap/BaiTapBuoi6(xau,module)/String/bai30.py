# def NegativeNumberlnString(s):
#     isNegative = False
#     num = 0
#     lst = []
#     for i in range(len(s)):
#         if s[i] == '-':
#             if i + 1 < len(s) and s[i + 1].isdigit():
#                 isNegative = True
#                 num = 0
#         elif s[i].isdigit():
#             num = num * 10 + int(s[i])
#         else:
#             if isNegative:
#                 lst.append(-num)
#                 num = 0
#                 isNegative = False

#     # kiem tra cuoi chuoi 
#     if isNegative:
#         lst.append(-num)
#     return lst

# s = input("s: ")
# print(NegativeNumberlnString(s))