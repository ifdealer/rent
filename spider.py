import bs4, re, requests
import csv
from requests import RequestException

page = 1


csv_file = open("rent.csv","w")
csv_write = csv.writer(csv_file,delimiter = ',')

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://gz.ziroom.com/z/nl/z2.html',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

def find_house(url):
    response = requests.get(url, headers=header)

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    item = soup.find_all('li', attrs={'class': 'clearfix'})
    patterns = re.compile(r'\[(.*?)\]')

    for i in item:
        detail = i.find('h3').text
        loca = i.find('h4').text
        loca = re.match(patterns, loca).group(1)
        url = i.find('a', attrs={'class': 't1'}).get('href')
        url = 'http:' + url
        print(loca)
        print(detail)
        print(url)
        csv_write.writerow([detail, loca, url])

for i in range(0,50):
    url = 'http://sz.ziroom.com/z/nl/z3.html?p=' + str(page)
    print(url)
    find_house(url)
    page = page+1

csv_file.close()
