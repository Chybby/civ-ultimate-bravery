#!/usr/bin/python

#TODO: fix up my images
#TODO: get a domain
#TODO: make victory type images
#TODO: religion images

import cgi
import random
import sys
import sqlite3
from jinja2 import Environment, FileSystemLoader

# bug checking
import cgitb
cgitb.enable()

# connect to the db
con = sqlite3.connect("civ.db")

# factory for results from the db
def dict_factory(cursor, row):
  d = {}
  for idx, col in enumerate(cursor.description):
      d[col[0]] = row[idx]
  return d

con.row_factory = dict_factory

# jinja2 environment and context
env = Environment(loader = FileSystemLoader('templates'))
context = {}

# get the arguments
query_args = cgi.FieldStorage()
section = query_args.getfirst('section', '')

content = ''

# returns a random from from the given table
def get_random_row(table):
  l = con.execute('SELECT COUNT(*) as n FROM %s' % table).fetchone()['n']
  return con.execute('SELECT * FROM %s WHERE id=?' % table, (random.randint(1, l),)).fetchone()

if section == 'religion':
  # return only the religion section
  context['religion'] = get_random_row('Religion')
  context['pantheon'] = get_random_row('Pantheon')
  context['founder'] = get_random_row('Founder')
  # we don't want two of the same follower beliefs
  l = con.execute('SELECT COUNT(*) as n FROM Follower').fetchone()['n']
  followers = random.sample(xrange(1, l+1), 2)
  context['follower1'] = con.execute('SELECT * FROM Follower WHERE id=?', (followers[0],)).fetchone()
  context['follower2'] = con.execute('SELECT * FROM Follower WHERE id=?', (followers[1],)).fetchone()
  context['enhancer'] = get_random_row('Enhancer')

  template = env.get_template('religion.html')
  content = template.render(context)
else:
  # return the whole page

  # randomise all the things
  context['civ'] = get_random_row('Civ')
  context['victory'] = get_random_row('Victory')
  # return only the religion section
  context['religion'] = get_random_row('Religion')
  context['pantheon'] = get_random_row('Pantheon')
  context['founder'] = get_random_row('Founder')
  # we don't want two of the same follower beliefs
  l = con.execute('SELECT COUNT(*) as n FROM Follower').fetchone()['n']
  followers = random.sample(xrange(1, l+1), 2)
  context['follower1'] = con.execute('SELECT * FROM Follower WHERE id=?', (followers[0],)).fetchone()
  context['follower2'] = con.execute('SELECT * FROM Follower WHERE id=?', (followers[1],)).fetchone()
  context['enhancer'] = get_random_row('Enhancer')
  context['policy_tree'] = get_random_row('PolicyTree')
  context['ideology'] = get_random_row('Ideology')

  template = env.get_template('main.html')
  content = template.render(context)

print 'Content-Type: text/html'
print
print content