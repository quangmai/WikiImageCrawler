#!/usr/bin/ruby
# -*- encoding : utf-8 -*-

require './lib/wp2txt.rb'
require 'mysql'


def time_diff_milli(start, finish)
       (finish - start) * 1000.0
end


# MySQL test

begin
    # connect to the MySQL server
	dbh = Mysql.real_connect("localhost", "root", "Fgla4Zp0", "javawiki")
	dbh.query_with_result = false

	#step = 1000
	#offset = 0
	count = 0
	time = Time.now

	# Generate Query
	qs = %{
SELECT
	p.page_id AS "Page ID",
	p.page_title As "Title",
	t.old_text AS "Text"
FROM
	page p
	INNER JOIN revision r
		ON p.page_latest = r.rev_id
	INNER JOIN text t
		ON r.rev_text_id = t.old_id
	INNER JOIN inv_index i
		ON p.page_id = i.page_id
WHERE
	i.inv_word = "mining" and
	p.page_namespace = 0 }

	# Get result set
	dbh.query(qs)
	res = dbh.use_result

	puts "<eecs485_articles>"

	# Process Generated Set
	while row = res.fetch_row do
		# printf "%s, %s\n", row["Page ID"], row["Text"]
		id = row[0]
		t = row[2] 
		title = row[1]

		t = dehtml(t)
		t = dewiki(t)

		puts "<eecs485_article>"
		puts "<eecs485_article_id>" + id + "</eecs485_article_id>"
		puts "<eecs485_article_title>" + title + "</eecs485_article_title>"
		puts "<eecs485_article_body>" + t + "</eecs485_article_body>"
		puts "</eecs485_article>"

		# print out speed of insertion
		count += 1 
		metronome = 1000
		if count%metronome == 0 then
			$stderr.puts count.to_s() + " (" + (metronome/time_diff_milli(time, Time.now)*1000).to_s() + "/sec)"
			time = Time.now
		end 
	end

	puts "</eecs485_articles>"

	# Free Result Set
	res.free 

	# Increase Offset
	#offset = offset + step
	#end

rescue Mysql::Error => e
    puts "Error code: #{e.errno}"
    puts "Error message: #{e.error}"
    puts "Error SQLSTATE: #{e.sqlstate}" if e.respond_to?("sqlstate")
ensure
    # disconnect from server
    dbh.close if dbh
end

