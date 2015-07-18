#!/usr/bin/python
# -*- coding: utf-8 -*-

from DTCScrapper import DTCScrapper
import sys

user_limit = sys.argv[1]

e = DTCScrapper()
url_dtc = "http://danstonchat.com/"+str(user_limit)+".html"

print("Quote n°"+ str((url_dtc.replace("http://danstonchat.com/","").replace(".html",""))))
print("==================")
try:
    for a in e.main(url_dtc):
        print(unicode(a))
    print("==================")
except:
    pass
