import re,requests
def idExtractor(s):
    #URL?
    if isURL(s):
        return getIDfromURL(s)
    #Short URL?
    elif isShortURL(s):
        return getIDfromShortURL(s)
    #Assume ID
    else:
        return s

def playlistIdExtractor(s):
    #Direct Link
    if isPlaylistUrl(s):
        return getList(s)
    #Video from playlist
    elif isURL(s):
        return getList(s)
    #Video from playlist with short link
    elif isShortURL(s):
        return getList(s)
    #Assume ID
    else:
        return s

def channelExtractor(s):
    #Link
    if isURL(s):
        return getUserFromUrl(s)

    #Assume ID
    else:
        return s

def isURL(s): 
    return (s.find("www.youtube.com") != -1)
def isShortURL(s):
    return (s.find("youtu.be") != -1)
def isPlaylistUrl(s):
    return (s.find("www.youtube.com/playlist") != -1)
def getUserFromUrl(s):
    splitUp=s.split('/')
    #print(splitUp[splitUp.index('user')+1])
    return splitUp[splitUp.index('user')+1]

def getIDfromURL(s):
    try:
        return re.findall(r'v=[^&#]+',s)[0][2:]
    except:
        return None
    
def getIDfromShortURL(s):
    if(s.find("?")!=-1):
        return  s[ s.find("/", s.find("/")+2)+1 :  s.find("?")] 
    return  s[ s.find("/", s.find("/")+2)+1  :  ]

def getList(s):
    try:
        return re.findall(r'list=[^&#]+',s)[0][5:]
    except:
        return None
"""
def getPLList(s):
    try:
        s=s[s.find('/playlist')+10:]
        print(s)
        return re.findall(r'list=[^&#]+',s)[0][2:]
    except:
        return None
"""

def videoUnavailable(id):
    r=requests.get("http://youtu.be/{}".format(id))
    if r.status_code != 200:
        return False
    if r.text.find("unavailable-message") != -1:
        return True
    return False