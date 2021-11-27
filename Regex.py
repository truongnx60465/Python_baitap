import re
f = open("place_code.txt", "r") 
# print(f.read())
fileJPG = re.compile(r'((\/[a-z\-]+)+\.jpg)')
matches = re.findall(fileJPG, f.read())
# print(('List match: ',  [m[0] for m in matches]))

protocol = "http:"
host = re.compile(r'(\d.\d.\d.\d)')
checkhost = re.findall(host, f.read())
print([a[1] for a in checkhost])

url = []
not_over_lapped = []
for m in matches:
	if m[0] not in not_over_lapped:
		not_over_lapped.append(m[0])

for s in not_over_lapped:
    newURL = protocol + s
    url.append(newURL)

print(url)
# print(not_over_lapped)