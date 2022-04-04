from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
 
url = 'http://py4e-data.dr-chuck.net/comments_1501365.xml'
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'lxml')
count = soup.find_all('count')
total = sum(int(i.text) for i in count)
print(f'The sum of all count in doc are: {total}')