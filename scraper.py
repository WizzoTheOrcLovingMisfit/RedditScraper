import socket
import re
import requests
from urllib.parse import urlparse
import html2text


def fix_karma(karma_list):
    purged=[]
    count=0
   
    while (count+2!=len(karma_list)):
        if karma_list[count] in (karma_list[count+1] and karma_list[count+2]) :
            purged.append(karma_list[count])
               
                
            count+=1
        else:
            
            count+=1
    
    return purged

'''Receieves all post urls for web page using regex of old.reddit.com/r/followed by any alpha numeric or _ + and then newline joins them'''
def get_posts(webpage):
       
    posts=re.findall("old.reddit.com\/r\/[a-zA-Z0-9_/]+\/[a-zA-Z0-9_/]+\/[a-zA-Z0-9_/]+", str(webpage))
    print('There are ' + str(len(posts)) + ' posts. The following posts were found:\r\n') 
    posts="\n".join(posts)
      
    return posts

''' returns the first post url for web page using regex of old.reddit.com/r/followed by any alpha numeric or _ +'''
def get_first_post(webpage):

    print('Tzshe first post of the page is: \r\n')
    first_post=re.search("old.reddit.com\/r\/[a-zA-Z0-9_/]+\/[a-zA-Z0-9_/]+\/[a-zA-Z0-9_/]+", str(webpage))

    return first_post.group()

'''Receieves all reddit users  urls for web page using regex of old.reddit.com/r/followed by any alpha numeric + and then newline joins them'''
def get_users(webpage):
    
    users=re.findall('reddit.com/user/[a-zA-Z0-9]+', str(webpage))
    print('There are ' + str(len(users)) + ' users. The following users were found:\r\n') 
    users="\n".join(users)

    return users

def get_first_user(webpage):

    print('The first user was: \r\n') 
    first_user=re.search('reddit.com/user/[a-zA-Z0-9]+', str(webpage))
    
    return first_user.group()

'''Receieves all subredditreddit urls for web page using regex of /r/ followed by any char + and then newline joins them'''
'''The amount of subs doesnt make sense, probably fix by stealing subreddit logic for first'''
def get_subreddits(webpage): 
    
    subreddits=re.findall('(?:/r)(/\w+\/)(?:comments)', str(webpage))
    print("there are " + str(len(subreddits)) + " following subreddit are referenced here\r\n")
    subreddits="\n".join(subreddits)
    return subreddits

'''Receieves all subredditreddit urls for web page using regex of /r/ followed by any char + and then newline joins them'''
def get_first_subreddit(webpage): 
    print("the following subreddits is found here\r\n")
    subreddit=re.search('(?:/r)(/\w+\/)(?:comments)', str(webpage))

    return subreddit.group(1)

def get_karma(webpage):
    
    karmascore=re.findall('\d+\.\dk', str(webpage))
    print("there are " + str(len(karmascore)) + " karma scores for the posts on this page are :\r\n")
    print("the purged score should be " + str(len(karmascore)/3) + " but is: " + str(len(fix_karma(karmascore))))
    karmascore=fix_karma(karmascore)
    
    karmascore="\n".join(karmascore)
    

    return karmascore

def get_first_karma(webpage):
    print("the first posts karma is:\r\n")
    karmascore=re.search('\d+\.\dk', str(webpage))
    

    return karmascore.group()

url = 'https://old.reddit.com/r/all/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
get_request=html2text.html2text(requests.get(url,headers=headers).text)
print("The page shows:\r\n")
print(get_request)

'''loop to constantly ask for input for testing purpose and direction of testing methods'''
while 1:

    option = input("Are you interested in users or posts or subs? ")

    if 'fpost' in option: 
        fpost = get_first_post(get_request)
        print(fpost + '\r\n') 

    elif 'post'  in option:
        posts=get_posts(get_request)
        print(posts + '\r\n')
        
    elif 'fuser' in option:
        fuser=get_first_user(get_request)
        print(fuser + '\r\n')

    elif 'user' in option:
        users=get_users(get_request)
        print(users + '\r\n')

    elif 'fsub' in option:
        subreddit=get_first_subreddit(get_request)
        print(subreddit) 

    elif 'sub' in option:
        subreddits=get_subreddits(get_request)
        print(subreddits + '\r\n') 

    elif 'fkarma' in option:
        karma=get_first_karma(get_request)
        print(karma + '\r\n') 

    elif 'karma' in option:
        karma=get_karma(get_request)
        print(karma + '\r\n') 

    else:
        break
    
    option=""






