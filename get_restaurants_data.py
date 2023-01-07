from requests import get
from bs4 import BeautifulSoup as Soup
from datetime import datetime
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-PDC6CGI\SQLEXPRESS;Database=testdb;Trusted_Connection=yes;')
cursor = conn.cursor()

cursor.execute('Select * from talabat_restaurants_urls where [done] is null')
c = 0

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)

for row in cursor.fetchall():
    c += 1
    url = 'https://www.talabat.com' + str(row[1])
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://cssspritegenerator.com',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    d = get(url, headers=hdr)
    soup = Soup(d.content, 'html.parser')

    html_element = soup.findAll('h1')
    text = 'h1'
    for i, line in enumerate(html_element):
            intStart = str(line).find('mt-2">') + len('mt-2">')
            line_str = str(line)
            line_str = line_str[intStart:]
            intEnd = line_str.find('</')
            entry_name = line_str[:intEnd]
            #print(entry_name)

    html_element = soup.findAll('p')
    text = 'cuisine-string white'
    for i, line in enumerate(html_element):
        if str(line).find(text) > 1:
            intStart = str(line).find('white">') + len('white">')
            line_str = str(line)
            line_str = line_str[intStart:]
            intEnd = line_str.find('</p')
            category_name = line_str[:intEnd]
            #print(category_name)

    html_element = soup.findAll('div')
    text = '<div class="rating-number text-center mr-1">'
    for i, line in enumerate(html_element):
        if str(line).find(text) > 1:
            intStart = str(line).find('center mr-1">') + len('center mr-1">')
            line_str = str(line)
            line_str = line_str[intStart:]
            intEnd = line_str.find('</div')
            rating = float(line_str[:intEnd])
            #print(rating)
            break

    html_element = soup.findAll('div')
    text = 'ratings-count ml-1'
    for i, line in enumerate(html_element):
        if str(line).find(text) > 1:
            intStart = str(line).find('ml-1">( ') + len('ml-1">( ')
            line_str = str(line)
            line_str = line_str[intStart:]
            intEnd = line_str.find(' Ratings')
            rated = int(line_str[:intEnd])
            #print(rated)
            break

    html_element = soup.findAll('span')
    text = 'f-500 ml-1'
    for i, line in enumerate(html_element):
        if str(line).find(text) > 1:
            intStart = str(line).find('ml-1">') + len('ml-1">')
            line_str = str(line)
            line_str = line_str[intStart:]
            intEnd = line_str.find(' Reviews')
            reviewed = int(line_str[:intEnd])
            #print(reviewed)
            break

    desc_msg = ''        
    html_element = soup.findAll('div')
    text = 'markdown-rich-text-block'
    for i, line in enumerate(html_element):
        if str(line).find(text) > 1:
            intStart = str(line).find('block"><p>') + len('block"><p>')
            line_str = str(line)
            line_str = line_str[intStart:]
            intEnd = line_str.find('</div>')
            desc_msg = line_str[:intEnd]
            desc_msg = desc_msg.replace('<p>','')
            desc_msg = desc_msg.replace('</p>','')
            #print(desc_msg)
            break
    
    insert_command = "Insert Into talabat_restaurants (entry_name, category, rating, rated, reviewed, descriptive_message, link_id) values ("
    insert_command += "'" + entry_name.replace("'","") + "', '" + category_name.replace("'","") + "', " + str(rating) + ", " + str(rated) + ", " + str(reviewed) + ", '" + (desc_msg.replace("'",'')).replace('','') + "', " + str(row[0]) + ")"
    print(url)
    # print(insert_command)
    cursor.execute(insert_command)
    conn.commit()

    update_command = 'Update talabat_restaurants_urls Set [done] = 1 where id = ' + str(row[0])
    cursor.execute(update_command)
    conn.commit()

print('\n' +str(c) + ' records inserted!')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print(current_time)

x = input('press Enter to close this window')