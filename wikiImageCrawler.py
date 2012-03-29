#!/usr/bin/python

import urllib2
import re
import sys
from pageTitleSelector import getPageIDandTitle

cursor = getPageIDandTitle("mining")
counter = 0

print "<eecs485_pa6_images>"

while (1):
	row = cursor.fetchone()
	if row == None:
		break

	counter += 1

	url_prefix = "http://en.wikipedia.org/wiki/"
	pageID = row[0]
	keyword = row[1]
	url = url_prefix + keyword


	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]

	try:
		infile = opener.open(url)
	except:
		sys.stderr.write("Could not connect to %s\n" % url)
		continue

	page = infile.read()
	match = re.findall(r"<img.*?src=[\"'](.+?)[\"']", page)

	print "<eecs485_image>"
	print "<eecs485_article_id>" + str(pageID) + "</eecs485_article_id>"
	print "<eecs485_article_title>" + keyword + "</eecs485_article_title>"
	print "<eecs485_pngs>"

	for m in match:
		xmlImagePrefix = "<eecs485_png_url>"
		xmlImageSuffix = "</eecs485_png_url>"
		print xmlImagePrefix + "http:" + m + xmlImageSuffix

	print "</eecs485_pngs>"
	print "</eecs485_image>"

	if counter%10 == 0:
		sys.stderr.write("%d pages have been processed\n" % counter)

print "</eecs485_pa6_images>"
