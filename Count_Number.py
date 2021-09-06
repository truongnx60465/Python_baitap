print("Đếm số")
my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
# lọc ra các số không trùng nhau
chuoi = set(my_list)
for i in chuoi:
   print(((i,my_list.count(i))))

# Em không gán lại bằng kiểu dict được , đã thử print(dict((i,my_list.count(i)))) , nhờ thầy sửa bài giùm
