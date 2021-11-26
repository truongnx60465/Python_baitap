import re
f = open("place_code.txt", "r") 
# print(f.read())
fileJPG = re.compile(r'(\/\/*\.)(?:jpg)')
match_obj = re.findall(fileJPG, f.read())
print(('List match: ' + match_obj.group()))
