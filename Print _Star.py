print("Print Star")
int_number1 = input("Nhập vào số dòng: ")
int_check = int(int_number1)
star = ' *'
space = " "
for i in range(0,int_check+1):
    print(space*(int_check-i)+star*i)
print("         ")
for i in range (1,int_check+1):
    print('  '*(i-1),'* '*(int_check+1-i))
print("         ")
for i in range (1,int_check+1):
    print('  '*(int_check-i),'* '*i)
print("         ")
for i in range (1,int_check+1):
    print('  '*(int_check-i),'* '*(2*i-1),'  '*(int_check-i))
print("         ")
for i in range (1,int_check+1):
    print('* '*int_check)
