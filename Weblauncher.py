from sys import *
import webbrowser
import re 
import urllib2

def is_connected():
    try:
        urllib2.urlopen("http://216.58.192.142",timeout=1)
        return True
    except urllib2.URLError as err:
        return False
        
def find(string):
    url=re.findall("^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$",string)
    return url
