print("Bài tập OOP - Buổi 2 - Magic methods")
int_number1 = int(input("Nhập vào tử số : "))
int_number2 = int(input("Nhập vào mẫu số: "))
class Fraction():
    def __init__(self, int_number1, int_number2):
        self._int_number1 = int_number1
        self._int_number2 = int_number2

    def display(self):
        if self._int_number2 < 0:
            print("-",self._int_number1,"/",abs(self._int_number2))
        else:
            print(self._int_number1,"/",self._int_number2)

def hcf(int_number1,int_number2):
    if int_number2 == 0:
        return print(int_number1)
    return hcf(int_number2, int_number1%int_number2)

def reduce (a,b,c):
    tuso = a / c
    mauso = b / c
    print(tuso,"/",mauso)

ps = Fraction(int_number1,int_number2)
ps.display()
hcf(int_number1,int_number2)
# Rút gọn phân số bị lỗi
reduce(int_number1,int_number2,int(hcf(int_number1,int_number2)))
