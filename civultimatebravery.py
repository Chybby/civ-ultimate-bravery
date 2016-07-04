# TODO: fix up my images
# TODO: religion images

import random
import sqlite3
from flask import (
    Flask,
    g,
    render_template,
    request,
)

from config import DATABASE

app = Flask(__name__)
app.config.from_object('config')


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def dict_factory(cursor, row):
    # factory for results from the db
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_random_row(cur, table):
    # returns a random row from the given table
    l = cur.execute('SELECT COUNT(*) as n FROM %s' % table).fetchone()['n']
    return cur.execute('SELECT * FROM %s WHERE id=?' % table, (random.randint(1, l),)).fetchone()


def generate_religion(cur):
    template_context = {}

    template_context['religion'] = get_random_row(cur, 'Religion')
    template_context['pantheon'] = get_random_row(cur, 'Pantheon')
    template_context['founder'] = get_random_row(cur, 'Founder')
    # we don't want two of the same follower beliefs
    l = cur.execute('SELECT COUNT(*) as n FROM Follower').fetchone()['n']
    followers = random.sample(xrange(1, l + 1), 2)
    template_context['follower1'] = cur.execute('SELECT * FROM Follower WHERE id=?', (followers[0],)).fetchone()
    template_context['follower2'] = cur.execute('SELECT * FROM Follower WHERE id=?', (followers[1],)).fetchone()
    template_context['enhancer'] = get_random_row(cur, 'Enhancer')

    return template_context


@app.route('/', methods=['GET'])
def homepage():
    # connect to the db
    cur = get_db().cursor()
    cur.row_factory = dict_factory

    template_context = {}

    section = request.args.get('section', '')

    if section == 'religion':
        # return only the religion section

        template_context = generate_religion(cur)
        return render_template('religion.html', **template_context)
    else:
        # return the whole page

        # randomise all the things
        template_context['civ'] = get_random_row(cur, 'Civ')
        template_context['victory'] = get_random_row(cur, 'Victory')

        template_context.update(generate_religion(cur))

        template_context['policy_tree'] = get_random_row(cur, 'PolicyTree')
        template_context['ideology'] = get_random_row(cur, 'Ideology')

        return render_template('main.html', **template_context)

if __name__ == '__main__':
    app.run()
