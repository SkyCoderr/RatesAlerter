from bs4 import BeautifulSoup
from urllib import request
from urllib import parse

url = "https://srh.bankofchina.com/search/whpj/search_cn.jsp"
Form_Data = {}
Form_Data['erectDate'] = ''
Form_Data['nothing'] = ''
Form_Data['pjname'] = '英镑'
data = parse.urlencode(Form_Data).encode('utf-8')
html = request.urlopen(url,data).read()
soup = BeautifulSoup(html,'html.parser')

div = soup.find('div', attrs = {'class':'BOC_main publish'})
table = div.find('table')
tr = table.find_all('tr')
td = tr[1].find_all('td')
print(td[0].get_text(),td[1].get_text(),td[2].get_text(),td[3].get_text(),td[4].get_text(),td[5].get_text(),td[6].get_text())

tr = table.find_all('tr')
for index in range(len(tr)):
    td = tr[index].find_all('td')
    print(td)

#tr = table.find_all('tr')
#for row in tr:
    #td = row.find_all('td')
    #print(td[0].get_text(),td[1].get_text(),td[2].get_text(),td[3].get_text(),td[4].get_text(),td[5].get_text(),td[6].get_text())