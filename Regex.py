import re
urls = []
path_pattern = re.compile(r'((\/[a-z\-]+)+\.jpg)')
host_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')
with open('place_code.txt', 'r') as f:
	for line in f.readlines():
		matches = re.findall(path_pattern, line)
		if len(matches) >= 1:
			path = matches[0][0]
		else:
			continue
		hosts = re.findall(host_pattern, line)
		if len(hosts) >= 2:
			host = hosts[-1]
			url = "http://{}{}".format(host, path)
			if url not in urls:
				urls.append(url)
print(urls)	