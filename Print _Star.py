print("Print Star")
int_number1 = input("Nhập vào số dòng: ")
int_check = int(int_number1)
star = '*'
space = " "
for i in range(0,int_check+1):
    print(space*(int_check-i)+star*i)

