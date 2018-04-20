from googlesearch import search

finput = open("input.txt","r")
names = []
for line in finput.readlines():
	names.append(line.rstrip())
f = open("output.txt","w+")
for name in names:
	links = list(search(name, tld = 'com', lang = 'en' , num = 5, start = 0 , stop = 5, pause = 2.0))
	linkName = "N/A"
	for link in links:
		if "www.ratemyprofessors.com/ShowRatings" in link:
			linkName = link
			break
	f.write(linkName + "\n")
f.close()
