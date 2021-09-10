print("Print Value from dict")
print("Cho dict có sẵn : unique_value_dict([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)])")
unique_value_dict = ([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)])
ans = set()
for i in unique_value_dict:
    for f in i.values():
        ans.add(f)
print(ans)