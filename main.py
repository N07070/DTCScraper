#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This script gets all the quotes from danstonchat, the french quote website.
"""

from bs4 import BeautifulSoup
import urllib2
import re

url_dtc = "http://danstonchat.com/12.html"
elements = []
list_links = []
liste_quote = []


class DTCScrapper(object):
    """docstring for DTCScrapper"""

    def get_web_page_content(self,url):
        web_page_content = ""
        try:
            web_page_content = urllib2.urlopen(url)
        except:
            print("Error, I could not the content from the page" + str(url))

        print("I got the content from " + str(url))
        return web_page_content

    def extract_quote_from_html(self,html_page,url):
        mushroomsoup = BeautifulSoup(html_page)
        for every_content in mushroomsoup.find('a',{'href':url}):
            every_content =  unicode(every_content).replace('<span class="decoration">',"")
            every_content =  unicode(every_content).replace('</span>',"")
            every_content =  unicode(every_content).replace('<br/>',"")
            if every_content == '' or every_content == " ":
                pass
            else:
                elements.append(every_content)

        return elements

    def main(self):
        return self.extract_quote_from_html(self.get_web_page_content(url_dtc),url_dtc)

e = DTCScrapper()

for a in e.main():
    print(unicode(a))
