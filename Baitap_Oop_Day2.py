def hcf(x, y):
    x, y = abs(x), abs(y)
    hcf = x if x < y else y

    while hcf > 0:
        if x % hcf == 0 and y % hcf == 0:
            break

        hcf -= 1

    return hcf if hcf > 0 else None


class Fraction:
    def __init__(self, nr, dr=1):
        if dr == 0:
            raise ZeroDivisionError("Mẫu số phải khác 0")

        if dr < 0:
            self.nr = nr * -1
            self.dr = dr * -1
        else:
            self.nr = nr
            self.dr = dr

        self._reduce()

    def __repr__(self):
        return "0" if self.nr == 0 else str(self.nr) if self.dr == 1 else f"{self.nr}/{self.dr}"

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction((self.nr * other.dr) + (other.nr * self.dr), self.dr * other.dr)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction((self.nr * other.dr) - (other.nr * self.dr), self.dr * other.dr)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction(self.nr * other.nr, self.dr * other.dr)

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction(self.nr * other.dr, other.nr * self.dr)

    def _reduce(self):
        n = hcf(self.nr, self.dr)

        if n:
            self.nr = int(self.nr / n)
            self.dr = int(self.dr / n)

print("Bài tập OOP - Buổi 2 - Magic methods")
int_number1 = int(input("Nhập vào tử số : "))
int_number2 = int(input("Nhập vào mẫu số: "))
number1 = Fraction(int_number1,int_number2)
print("Số vừa nhập: ",number1)
number2 = Fraction(1.5,-3)
print("Set default số thứ 2 sau khi rút gọn Fraction(1.5,-3) là :", number2)
print("Số thứ nhất + số thứ 2 = ",number1 + number2)
print("Số thứ nhất - số thứ 2 = ",number1 - number2)
print("Số thứ nhất * số thứ 2 = ",number1 * number2)
print("Số thứ nhất / số thứ 2 = ",number1 / number2)