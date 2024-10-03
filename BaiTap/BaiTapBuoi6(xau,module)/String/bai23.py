
    

# def solve(s):
#     indexA = s.find('@')
#     indexP = s.find('.')

#     a = s[0:indexA]
#     b = s[indexA+1:indexP]
#     c = s[indexP+1::]

#     con_1 = len(a) != 0 and len(b) != 0 and len(c) != 0

#     # replace('.', '').replace('-', '').isalnum(): Cho phép dấu chấm và dấu gạch
#     #  ngang trong các phần tên và miền,
#     # nhưng tất cả các ký tự khác phải là chữ cái hoặc số.
#     con_2 = a.replace('-','').replace('.','').isalnum() and \
#             b.replace('-','').replace('.','').isalnum() and \
#             c.isalpha()

#     con_3 = s.count('@') == 1 and s.count('.') == 1

#     return con_1 and con_2 and con_3

# s = input("s: ")
# result = solve(s)
# print("VALID") if result == True else print("INVALID")
