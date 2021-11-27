import re
f = open("place_code.txt", "r") 
# print(f.read())
fileJPG = re.compile(r'((\/[a-z\-]+)+\.jpg)')
matches = re.findall(fileJPG, f.read())
print(('List match: ',  [m[0] for m in matches]))
