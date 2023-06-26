import requests
from bs4 import BeautifulSoup
from beautiful_date import * 
from dateutil import parser
import sys

def tableDataText(table):    
    """Parses a html segment started with tag <table> followed 
    by multiple <tr> (table rows) and inner <td> (table data) tags. 
    It returns a list of rows with inner columns. 
    Accepts only one <th> (table header/data) in the first row.
    """
    def rowgetDataText(tr, coltag='td'): # td (data) or th (header)       
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]  
    rows = []
    trs = table.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append(rowgetDataText(tr, 'td') ) # data row       
    return rows

def convertToBeautifulDate(date):
    if not isinstance(date, str):
        print(f"convertToBeautifulDate() has received a {type(date) = } instead of a String.")
        return
    try: 
        parsed_date = parser.parse(date)
        return BeautifulDate(parsed_date.year, parsed_date.month, parsed_date.day)
    except: 
        return 


url = "https://starwars.fandom.com/wiki/List_of_future_comics"
html = requests.get(url, auth=("user", "pass")).text
future_swcomics_html = BeautifulSoup(html, "html.parser")
table = future_swcomics_html.find(id="prettytable")
table = tableDataText(table)
table.pop(0)
current_date = D.today()
date_range = []
for i in range(7):
    date_range.append(current_date+i*days)


for row in table:
    title= row[0]
    type_comic = "Issue" if row[1].lower() == "comic book" else row[1].title()
    publish_date = convertToBeautifulDate(row[2])
    if not all([title, type_comic, publish_date]): 
        continue
    if publish_date in date_range: 
        print(f"{type_comic}:\t{title} [{publish_date}]")


