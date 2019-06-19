from urllib.request import Request,urlopen as uReq
from bs4 import BeautifulSoup as soup

req = Request('https://freelancehunt.com/projects/skill/parsing-dannyih/169.html?page=1',headers={'User-Agent': 'Mozilla/5.0'})
response = uReq(req)
page_html = response.read()
response.close()

page_soup = soup(page_html,'html.parser')

tr_list = page_soup.findAll('tr',{'style':'vertical-align: top'})
td_list = page_soup.findAll('td',{'class':'text-center'})


titles =[]

for tr in tr_list:
	title = tr.td.a.text
	titles.append(title)
	
price_list =[]
for td in td_list:
	remainder = td_list.index(td) % 4
	if remainder == 0:
		price_list.append(td.span.text.strip())


def final(titles,prices):
	x = 0
	lines = []
	while x <= len(titles)-1:
		line = titles[x] + ' --- ' + prices[x]
		lines.append(line)
		print(lines[x])
		x += 1
	return lines
		
lines = final(titles,price_list)
f = open('spider.txt','w')

for line in lines:
	line = line.replace('₴','GRN')
	f.write(line + '\n')

f.close()







