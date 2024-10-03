price = int(input('Nhap don gia: ')) 
count = int(input('Nhap so luong: ')) 
totalPrice = price * count
print('{:>30} {:>7}'.format('Tong tien truoc thue:',f'{totalPrice}'))
print('{:>30} {:>7}'.format('Thue:',f'{int(0.1*totalPrice)}'))
print('{:>30} {:>7}'.format('Sau thue:',f'{int(totalPrice)}'))