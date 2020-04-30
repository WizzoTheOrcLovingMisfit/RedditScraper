import socket
import re
import requests
from urllib.parse import urlparse
import html2text


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
url='https://old.reddit.com/user/memezzer/submitted/'
get_request=html2text.html2text(requests.get(url,headers=headers).text)
comment=re.findall('reddit.com/user/[a-zA-Z0-9].+\)', str(get_request))
top_post=re.findall('\(\/r\/*.+\/\))', str(get_request)))
print(get_request)
print('browsing to ' + url + ' and finding users') 
print(comment)
print(top_post)