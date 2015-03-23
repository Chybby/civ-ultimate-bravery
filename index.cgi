#!/usr/bin/python

# all the data about civilization
from data import *

import cgi
import random
import sys
from jinja2 import Environment, FileSystemLoader

# bug checking
import cgitb
cgitb.enable()

# jinja2 environment and context
env = Environment(loader = FileSystemLoader('templates'))
context = {}

# get the arguments
query_args = cgi.FieldStorage()
section = query_args.getfirst('section', '')

content = ''

if section == 'religion':
  # return only the religion section
  context['religion'] = random.choice(religions)
  context['pantheon'] = random.choice(pantheons)
  context['founder'] = random.choice(founder_beliefs)
  # we don't want two of the same follower beliefs
  followers = random.sample(follower_beliefs, 2)
  context['follower1'] = followers[0]
  context['follower2'] = followers[1]
  context['enhancer'] = random.choice(enhancer_beliefs)

  template = env.get_template('religion.html')
  content = template.render(context)
else:
  # return the whole page

  # randomise all the things
  context['civ'] = random.choice(civs)
  context['victory'] = random.choice(victories)
  context['religion'] = random.choice(religions)
  context['pantheon'] = random.choice(pantheons)
  context['founder'] = random.choice(founder_beliefs)
  # we don't want two of the same follower beliefs
  followers = random.sample(follower_beliefs, 2)
  context['follower1'] = followers[0]
  context['follower2'] = followers[1]
  context['enhancer'] = random.choice(enhancer_beliefs)
  context['policy_tree'] = random.choice(policy_trees)
  context['ideology'] = random.choice(ideologies)

  template = env.get_template('main.html')
  content = template.render(context)

print 'Content-Type: text/html'
print
print content