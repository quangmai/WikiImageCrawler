#!/usr/bin/python

import urllib2
import re

url_prefix = "http://en.wikipedia.org/wiki/"
keyword = "Alabama"
url = url_prefix + keyword

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
infile = opener.open(url)
page = infile.read()

match = re.findall(r"<img.*?src=[\"'](.+?)[\"']", page)

print "<eecs485_pngs>"

for m in match:
	xmlImagePrefix = "<eecs485_png_url>"
	print "http:" + m
	xmlImageSuffix = "</eecs485_png_url>"

print "</eecs485_pngs>"


