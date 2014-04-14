#!/usr/bin/python
# coding: utf-8

import re, urllib, urllib2, string, sys, os
from BeautifulSoup import BeautifulSoup

#Collect Bing Results For Term
def grepBing(searchTerm):
  user_agent = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'}
  #Requesting results from google, open, read data, close
  request = urllib2.Request(searchTerm, None, user_agent)
  urlLog = urllib2.urlopen(request)
  site = urlLog.read(200000)
  urlLog.close()
 
  soup = BeautifulSoup(site)
  links = [x.find('a')['href'] for x in soup.find('div', id='results').findAll('h3')]
  #As function exits, it passes data back to function call to fill file
  return links


#Check URL for SQLi Vuln
def checkVuln(website):
  EXT = "'"
  capture = urllib2.urlopen(website).read()
  bool = False
  check = "error in your SQL"
  if re.search(check, capture):
    bool = True
  print website
  print bool

def search(term):
  links = grepBing(term)
  for x in links:
    checkVuln(x)

search('http://www.bing.com/search?q=inurl:index.php?id=')
search('http://www.bing.com/search?q=inurl:index.php?id=&first=9')
