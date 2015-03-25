#!/usr/bin/python

#TODO: serve my own images
#TODO: use a database
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

# dict_factory for results from the db
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

num_civs = 43
num_victories = 5
num_religions = 13
num_pantheons = 26
num_founders = 16
num_followers = 9
num_enhancers = 9
num_policies = 3
num_ideologies = 3

if section == 'religion':
  # return only the religion section
  context['religion'] = con.execute('SELECT * FROM Religion WHERE id=?', (random.randint(1, num_religions),)).fetchone()
  context['pantheon'] = con.execute('SELECT * FROM Pantheon WHERE id=?', (random.randint(1, num_pantheons),)).fetchone()
  context['founder'] = con.execute('SELECT * FROM Founder WHERE id=?', (random.randint(1, num_founders),)).fetchone()
  # we don't want two of the same follower beliefs
  followers = random.sample(xrange(1,num_followers+1), 2)
  context['follower1'] = con.execute('SELECT * FROM Follower WHERE id=?', (followers[0],)).fetchone()
  context['follower2'] = con.execute('SELECT * FROM Follower WHERE id=?', (followers[1],)).fetchone()
  context['enhancer'] = con.execute('SELECT * FROM Enhancer WHERE id=?', (random.randint(1, num_enhancers),)).fetchone()

  template = env.get_template('religion.html')
  content = template.render(context)
else:
  # return the whole page

  # randomise all the things
  context['civ'] = con.execute('SELECT * FROM Civ WHERE id=?', (random.randint(1, num_civs),)).fetchone()
  context['victory'] = con.execute('SELECT * FROM Victory WHERE id=?', (random.randint(1, num_victories),)).fetchone()
  context['religion'] = con.execute('SELECT * FROM Religion WHERE id=?', (random.randint(1, num_religions),)).fetchone()
  context['pantheon'] = con.execute('SELECT * FROM Pantheon WHERE id=?', (random.randint(1, num_pantheons),)).fetchone()
  context['founder'] = con.execute('SELECT * FROM Founder WHERE id=?', (random.randint(1, num_founders),)).fetchone()
  # we don't want two of the same follower beliefs
  followers = random.sample(xrange(1,num_followers+1), 2)
  context['follower1'] = con.execute('SELECT * FROM Follower WHERE id=?', (followers[0],)).fetchone()
  context['follower2'] = con.execute('SELECT * FROM Follower WHERE id=?', (followers[1],)).fetchone()
  context['enhancer'] = con.execute('SELECT * FROM Enhancer WHERE id=?', (random.randint(1, num_enhancers),)).fetchone()
  context['policy_tree'] = con.execute('SELECT * FROM PolicyTree WHERE id=?', (random.randint(1, num_policies),)).fetchone()
  context['ideology'] = con.execute('SELECT * FROM Ideology WHERE id=?', (random.randint(1, num_ideologies),)).fetchone()

  template = env.get_template('main.html')
  content = template.render(context)

print 'Content-Type: text/html'
print
print content