
from bs4 import BeautifulSoup as bs
import urllib2
import re
# Get the content of all the elements in the page.


#page = urllib2.urlopen("/home/amitd92/solr/NYTimesData/NYTimesDownloadData/daf938d7-b7fc-4237-beed-fa64d84de9f5.html")

text=bs(open("/home/amitd92/solr/NYTimesData/NYTimesDownloadData/5348b1eb-5793-4b40-ae29-23c3006e29f1.html"),"lxml").find("body")
for x in text:
    print x
text =text.findAll(text=re.compile("/* wash/*", re.I))

print text



# Limit the content to the first 150 bytes, eliminate leading or
# trailing whitespace.
snippet = text[0:150]
snippet = " ".join(text.split()).strip()[0:150]


# If text was longer than this (most likely), also add '...'
if len(text) > 150:
  snippet += "..."

print snippet