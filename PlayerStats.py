# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 23:44:00 2016

@author: LinusZhao
"""
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import requests
r = requests.get('https://allthingsfpl.com/fantasy-footbal/opta-player-profile?player=p37265')
r.status_code

import bs4
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)


 
#---------------------------------import---------------------------------------
import urllib2
import re
from bs4 import BeautifulSoup
 
#------------------------------------------------------------------------------
#def main():
    userMainUrl = "https://allthingsfpl.com/fantasy-football/opta-player-zones/?club%5B%5D=ARS&played=0&week=2gw&custom_from=&custom_to=&season=0"
    req = urllib2.Request(userMainUrl)
    resp = urllib2.urlopen(req)
    respHtml = resp.read()
    #print "respHtml=",respHtml; # you should see the ouput html
 
    print "Method 2: Use python third lib BeautifulSoup to extract info from html"
    songtasteHtmlEncoding = "GB2312"
    soup = BeautifulSoup(respHtml, from_encoding=songtasteHtmlEncoding)
    #<h1 class="h1user">crifan</h1>
    foundClassH1user = soup.find(attrs={"class":"h1user"})
    print "foundClassH1user=%s",foundClassH1user
    if(foundClassH1user):
        h1userStr = foundClassH1user.string
        print "h1userStr=",h1userStr
 
###############################################################################
if __name__=="__main__":
    main()
