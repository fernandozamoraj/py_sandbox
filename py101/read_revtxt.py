from urllib.request import urlopen

def words_per_line(flo):
	#return [len(line.split()) for line in flo.readlines()]
    return [line for line in flo.readlines()]

with urlopen('https://pbusetest1.army.mil/rev.txt') as web_file:
	wpl = words_per_line(web_file)
		

print(wpl)