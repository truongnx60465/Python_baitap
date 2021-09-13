print("Xử lý chuỗi - Đảo ngược từ và kiểu hoa thường")
print("Cho chuỗi có sẵn : tHE fOX iS cOMING fOR tHE cHICKEN")
stringA = "tHE fOX iS cOMING fOR tHE cHICKEN"
stringB = stringA.swapcase()
# print(stringB)
stringC = stringB.split(" ")[::-1]
myString = " ".join(stringC)
print("Kết quả là: ",myString)