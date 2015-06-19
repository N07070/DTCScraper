#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This script gets all the quotes from danstonchat, the french quote website.
"""

from bs4 import BeautifulSoup
import urllib2

class DTCScrapper(object):
    """docstring for DTCScrapper"""
    # def __init__(self, arg):
    #     super(DTCScrapper, self).__init__()
    #     self.arg = arg

    def get_web_page_content(self,url):
        web_page_content = ""
        try:
            web_page_content = urllib2.urlopen(url)
        except:
            print("Error, I could not the content from the page" + str(url))

        print("I got the content from " + str(url))
        return web_page_content

    def extract_quote_from_html(self,html_page):
        soup = BeautifulSoup(html_page)
        soup = soup.select('div .item-content span')
        return soup

e = DTCScrapper()
derp = e.get_web_page_content("http://danstonchat.com/16561.html")
print(derp)
print(e.extract_quote_from_html(derp))

[<p class="item-content">
    <a href="http://danstonchat.com/16561.html">
        <span class="decoration">A:</span> Tout a leur, j'ai laissé ma soeur utiliser le pc.<br/>
        <span class="decoration">Z:</span> wow, quel courage!<br/>
        <span class="decoration">A:</span> Oui, rigole...<br/>
        <span class="decoration">A:</span> Je lui dit "pour scroller avec le touchpad, il faut utiliser les deux doitgs".<br/>
        <span class="decoration">A:</span> Elle m'a regardé bizarre...
    </a>
</p>]
