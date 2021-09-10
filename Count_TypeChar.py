print("Function - Đếm loại ký tự")
print("Cho chuỗi có sẵn : s = 'Hello World! 123'")
s = "Hello World! 123"
int_len = len(s)
ansSum = {}
ans = {}
def count_char_type(str):
    countUper = 0
    countLower = 0
    countDigit = 0
    for i in str:
        if i.isupper():
            countUper = countUper + 1
            ans["UPPERCASE"] = countUper
        if i.islower():
            countLower = countLower + 1
            ans["LOWERCASE"] = countLower
        if i.isdigit():
            countDigit = countDigit + 1
    ansSum["LETTERS"] = countUper + countLower
    ansSum["CASE"] = ans
    ansSum["DIGITS"] = countDigit
    print(ansSum)

count_char_type(s)