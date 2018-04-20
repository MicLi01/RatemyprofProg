from lxml import html
import requests
import sys

links = []
for line in sys.stdin:
	links.append(line[:len(line)-1])
for link in links:
	page = requests.get(link)
	tree = html.fromstring(page.content)
	grade = tree.xpath('//div[@class="grade"]/text()') 
	fname = tree.xpath('//span[@class="pfname"]/text()')
	lname = tree.xpath('//span[@class="plname"]/text()')
	print(fname[0].lstrip().rstrip(),lname[0].lstrip().rstrip(),":",end = " ") 
	grade[0] = "rating = " + grade[0].lstrip().rstrip()
	grade[1] = "WTA = " + grade[1].lstrip().rstrip()
	grade[2] = "Difficulty = " + grade[2].lstrip().rstrip()
	for i in grade:
		print(i,end = " ")
