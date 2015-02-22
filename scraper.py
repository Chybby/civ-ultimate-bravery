#!/usr/bin/python

# scrapes http://www.civfanatics.com/ and http://civilization.wikia.com/ for
# info about Civilization 5.
# some parts are slightly hardcoded but this is only run once to collect all the
# necessary data and is checked by hand before being used so it should be fine

civ_url = 'http://www.civfanatics.com/civ5/civilizations'

import urllib
import re

civ_html = urllib.urlopen(civ_url)

# find all the tables on the page
page_tables = re.findall(r'<table.*?>(.*?)</table>', civ_html.read(), re.S)

civ_table = page_tables[17]

# find all the table data
civ_raw_data = re.findall(r'<td.*?>(.*?)</td>', civ_table, re.S)[8:]

# the table data is grouped in groups of 7
civ_data = [{'civ_image':civ_raw_data[x],
             'name':re.sub(r'\s*\(.*\)\s*', '', civ_raw_data[x+1]),
             'leader_image':civ_raw_data[x+2],
             'leader':civ_raw_data[x+3],
             'ability_name':re.search(r'<b>(.*?):? ?</b>', civ_raw_data[x+4]).group(1),
             'ability_desc':re.sub(r'<b>.*?</b>:?\s*', '', civ_raw_data[x+4]),
             'unique1':civ_raw_data[x+5],
             'unique2':civ_raw_data[x+6]} for x in xrange(0,len(civ_raw_data),7)]

print civ_data

religion_url = 'http://civilization.wikia.com/wiki/Religion_(Civ5)'

religion_html = urllib.urlopen(religion_url)

# find all the tables on the page
religion_tables = re.findall(r'<table.*?>(.*?)</table>', religion_html.read(), re.S)

# identify each table found
pantheon_table = religion_tables[0]
founder_table = religion_tables[1]
follower_table = religion_tables[2]
enhancer_table = religion_tables[3]

for table in (pantheon_table, founder_table, follower_table, enhancer_table):
  # find all the table data in this table
  table_raw = re.findall(r'<td>(.*?)</td>', table, re.S)

  for i in xrange(len(table_raw)):
    # remove random html stuff from the description
    table_raw[i] = re.sub(r'</?(a|img|span|noscript).*?>', '', table_raw[i])
    # strip extra whitespace at either end and between words
    table_raw[i] = table_raw[i].strip()
    table_raw[i] = re.sub(r'\s+', ' ', table_raw[i])

  # the table data is grouped in groups of 2
  table = [{'name':table_raw[i], 'desc':table_raw[i+1]} for i in xrange(0, len(table_raw), 2)]

  #print table