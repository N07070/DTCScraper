#!/usr/bin/python
# -*- coding: utf-8 -*-

from DTCScrapper import DTCScrapper
import sys

# Get the quote number from the arguments
user_limit = sys.argv[1]

# Initiate the class
e = DTCScrapper()

# Create the url
url_dtc = "http://danstonchat.com/"+str(user_limit)+".html"

# Get the results
result_from_scrapper =  e.main(url_dtc)

# Print out each value
for value in result_from_scrapper:
    print(value)
