#!/usr/bin/python

import MySQLdb

def getPageIDandTitle(key):
	query = """
	SELECT
		p.page_id AS "Page ID",
		p.page_title As "Title"
	FROM
		page p
		INNER JOIN inv_index i
		ON p.page_id = i.page_id
	WHERE
		i.inv_word = "%s" and
		p.page_namespace = 0
	""" % key

	db = MySQLdb.connect(user="root",passwd="Fgla4Zp0",db="javawiki")
	c = db.cursor()
	c.execute(query)

	return c

