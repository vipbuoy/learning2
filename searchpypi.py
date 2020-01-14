#this program includes python project searching on pypi.org and google searching
#via including modules
import requests,googlesearch,webbrowser,bs4,time
find=input('What you wanna to be search:')
limit=int(input('How many projects you wanna open!'))
print('Searching...')
time.sleep(5)
print(f'Opening python  {limit} projects on {find}')
res=requests.get('https://pypi.org/search/?q='
+ find)
s=bs4.BeautifulSoup(res.text,'html.parser')
link=s.select('.package-snippet')
try:
 for i in range(limit):
     webbrowser.open('https://pypi.org'+link[i].get('href'))
     time.sleep(4)
except:
    print('No more projects present!')
else:
    print('Opened!')

time.sleep(10)
find=input('Enter what you wanna to search:')
print('Opening google search!')
for j in googlesearch.search(find,tld='com',num=limit,stop=limit,pause=2):
    webbrowser.open(j)
    time.sleep(4)
