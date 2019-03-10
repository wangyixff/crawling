from bs4 import BeautifulSoup


#parsing the html page content, reading the tables
x=download('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')
with open("toronto.html", "w") as file:
    file.write(x)

with open('toronto.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

table = soup.find('table',{'class':'wikitable sortable'})
trs = table.findAll('tr')

Neighbourhood = []
Postcode = []
Borough = []
df = pd.DataFrame()
for tr in trs:
    tds = tr.findAll('td')
    if len(tds):
        Postcode.append(tds[0].text)
        Borough.append(tds[1].text)
        Neighbourhood.append(tds[2].text.strip())
#strip is used to clear the text strings
df['Postcode'] = Postcode
df['Borough'] = Borough
df['Neighbourhood'] = Neighbourhood