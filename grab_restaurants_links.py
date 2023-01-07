from requests import get
from bs4 import BeautifulSoup as Soup
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-PDC6CGI\SQLEXPRESS;Database=testdb;Trusted_Connection=yes;')
cursor = conn.cursor()

url = "https://www.talabat.com/uae/restaurants"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://cssspritegenerator.com',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
page_refresh = 0
while True:
    d = get(url, headers=hdr)
    soup = Soup(d.content, 'html.parser')
    html_element = soup.findAll('a')
    text = '<div class="logo text-center'
    for i, line in enumerate(html_element):
        if str(line).find(text) > 1:
            intStart = str(line).find('<a href="') + len('<a href="')
            line_str = str(line)
            line_str = line_str[intStart:]
            intEnd = line_str.find('">')
            target_text = line_str[:intEnd]
            insert_cmd = "Insert Into talabat_restaurants_urls (url) values ('"  + target_text + "')"
            cursor.execute(insert_cmd)
            conn.commit()
            print(i, target_text)
    page_refresh += 1
    print(page_refresh)
    if page_refresh >= 5:
        break