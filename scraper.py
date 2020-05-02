import socket
import re
import requests
from urllib.parse import urlparse
import html2text


def cleanser(posts):
    bad_chars = ['(', ')']
    print(type(posts))
    for i in bad_chars : 
        print(i)
        posts = posts.replace(i, "") 
    return posts

def get_posts(webpage):
       print('The following posts were found') 
       posts=re.findall("old.reddit.com\/r\/[a-zA-Z0-9_/]+", str(webpage))
       posts="\n".join(posts)
      
       return posts

def get_users(webpage):
    print('The following users were found') 
    users=re.findall('reddit.com/user/[a-zA-Z0-9]+', str(webpage))
    users="\n".join(users)
    return users

def get_subreddits(webpage): 
    print("the following subewddits are referenced here")
    subreddits=re.findall('/r/\w+', str(webpage))
    subreddits="\n".join(subreddits)
    return subreddits

url = 'https://old.reddit.com/r/all/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}

get_request=html2text.html2text(requests.get(url,headers=headers).text)
print("The page shows:\r\n")
print(get_request)
while 1:
    option = input("Are you interested in users or posts or subs? ")
    if 'user' in option:

        users=get_users(get_request)
    
    
        print(users)
    elif 'post' in option:
        posts=get_posts(get_request)
    
    
        print(posts)

    elif 'reddit' in option:
        subreddits=get_subreddits(get_request)
    
    
        print(subreddits)
    else:
        break
    option=""






