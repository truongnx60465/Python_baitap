print("Function - Đếm loại ký tự")
print("Cho chuỗi có sẵn : s = 'Hello World! 123'")
s = "Hello World! 123"
int_len = len(s)
countUper = 0
ans = {}
def count_char_type(abc):
    for i in range(abc):
        if s[i].islower:
            countUper =+ 1
            ans["UPPERCASE"] = countUper
    print(ans)

count_char_type(int_len)