from lxml import html
import requests
import sys

f = open("output.txt","r")
input_links = f.readlines()
links = []
for line in input_links:
	links.append(line.rstrip())

rating_output = open("ratingout.txt","w+")
for link in links:
	if link == "N/A":
		rating_output.write("Not Found \n")
		continue
	page = requests.get(link)
	tree = html.fromstring(page.content)
	grade = tree.xpath('//div[@class="grade"]/text()')[:3] 
	fname = tree.xpath('//span[@class="pfname"]/text()')
	lname = tree.xpath('//span[@class="plname"]/text()')
	print(fname[0].lstrip().rstrip(),lname[0].lstrip().rstrip(),":",end = " ") 
	rating_output.write(fname[0].lstrip().rstrip() + " " + lname[0].lstrip().rstrip() + " ")
	grade[0] = "rating = " + grade[0].lstrip().rstrip()
	grade[1] = "WTA = " + grade[1].lstrip().rstrip()
	grade[2] = "Difficulty = " + grade[2].lstrip().rstrip()
	for i in grade:
		print(i,end = " ")
		rating_output.write(i + " ")
	rating_output.write("\n")
