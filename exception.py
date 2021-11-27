import random
class Error(Exception):
    """Base class cho các exception trong module"""
    pass
class NotIntegerError(Error):
    """Ném ra khi giá trị đầu vào không phải integer"""
    def __init__(self, value):
        message = f"Không phải số nguyên: {value}"
        self.value = value
        self.message = message

number = random.randint(0, 50)
print(number)
int_number1 = int(input("Nhập vào một số bất kỳ để so sánh: "))
if type(int_number1) != int: raise NotIntegerError(int_number1)
    pass
if number == int_number1:
    print("Hai số bằng nhau")
elif number > int_number1:
    print("Số vừa nhập nhỏ hơn số random")
elif number < int_number1:
    print("Số vừa nhập lớn hơn số random")