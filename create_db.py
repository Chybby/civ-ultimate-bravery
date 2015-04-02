#!/usr/bin/python

import os
import os.path
import sys

from data import *

import sqlite3

if os.path.isfile('civ.db'):
  os.remove('civ.db')

con = sqlite3.connect("civ.db")

con.execute('''CREATE TABLE Civ (
               id INT,
               name VARCHAR(20) NOT NULL,
               leader VARCHAR(30) NOT NULL,
               ability_name VARCHAR(40) NOT NULL,
               ability_desc VARCHAR(255) NOT NULL,
               unique1 VARCHAR(30) NOT NULL,
               unique2 VARCHAR(30) NOT NULL,
               leader_image VARCHAR(150) NOT NULL,
               civ_image VARCHAR(150) NOT NULL,
               PRIMARY KEY(id))''')

con.execute('''CREATE TABLE Victory (
               id INT,
               name VARCHAR(20) NOT NULL,
               vic_desc VARCHAR(100) NOT NULL,
               image VARCHAR(25) NOT NULL,
               PRIMARY KEY(id))''')

con.execute('''CREATE TABLE Religion (
               id INT,
               name VARCHAR(20) NOT NULL,
               PRIMARY KEY(id))''')

con.execute('''CREATE TABLE Pantheon (
               id INT,
               name VARCHAR(30) NOT NULL,
               pan_desc VARCHAR(150) NOT NULL,
               PRIMARY KEY(id))''')

con.execute('''CREATE TABLE Follower (
               id INT,
               name VARCHAR(20) NOT NULL,
               fol_desc VARCHAR(150) NOT NULL,
               PRIMARY KEY(id))''')

con.execute('''CREATE TABLE Founder (
               id INT,
               name VARCHAR(30) NOT NULL,
               foun_desc VARCHAR(150) NOT NULL,
               PRIMARY KEY(id))''')

con.execute('''CREATE TABLE Enhancer (
               id INT,
               name VARCHAR(30) NOT NULL,
               enh_desc VARCHAR(150) NOT NULL,
               PRIMARY KEY(id))''')

con.execute('''CREATE TABLE PolicyTree (
               id INT,
               name VARCHAR(10) NOT NULL,
               pol_desc VARCHAR(550) NOT NULL,
               PRIMARY KEY(id))''')

con.execute('''CREATE TABLE Ideology (
               id INT,
               name VARCHAR(10) NOT NULL,
               ide_desc VARCHAR(400) NOT NULL,
               PRIMARY KEY(id))''')

with con:
  # insert civ data
  i = 1
  for c in civs:
    con.execute('INSERT INTO Civ VALUES (?,?,?,?,?,?,?,?,?);', (i, c['name'], c['leader'], c['ability_name'], c['ability_desc'], c['unique1'], c['unique2'], c['leader_image'], c['civ_image']))
    i += 1

  # insert victory data
  i = 1
  for v in victories:
    con.execute('INSERT INTO Victory VALUES (?,?,?,?);', (i, v['name'], v['desc'], v['image']))
    i += 1

  # insert religion data
  i = 1
  for r in religions:
    con.execute('INSERT INTO Religion VALUES (?,?);', (i, r['name']))
    i += 1

  # insert pantheon data
  i = 1
  for p in pantheons:
    con.execute('INSERT INTO Pantheon VALUES (?,?,?);', (i, p['name'], p['desc']))
    i += 1

  # insert founder belief data
  i = 1
  for f in founder_beliefs:
    con.execute('INSERT INTO Founder VALUES (?,?,?);', (i, f['name'], f['desc']))
    i += 1

  # insert follower belief data
  i = 1
  for f in follower_beliefs:
    con.execute('INSERT INTO Follower VALUES (?,?,?);', (i, f['name'], f['desc']))
    i += 1

  # insert enhancer belief data
  i = 1
  for e in enhancer_beliefs:
    con.execute('INSERT INTO Enhancer VALUES (?,?,?);', (i, e['name'], e['desc']))
    i += 1

  # insert policy tree data
  i = 1
  for p in policy_trees:
    con.execute('INSERT INTO PolicyTree VALUES (?,?,?);', (i, p['name'], p['desc']))
    i += 1

  # insert ideology data
  i = 1
  for d in ideologies:
    con.execute('INSERT INTO Ideology VALUES (?,?,?);', (i, d['name'], d['desc']))
    i += 1