# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 10:22:53 2017

@author: 王喆
"""

from flask import Flask,request,render_template,Markup,session,redirect, url_for,make_response
from flask import abort,flash,g
import time
import sqlite3
import random

conn_db = False
app = Flask(__name__)

app.config.update(
    DATABASE = 'db/article.db',
    DEBUG = True,
    SECRET_KEY = 'secret_k_1'
)

@app.before_request
def before_request():
    g.db = sqlite3.connect('db/article.db')
    g.c = g.db.cursor()
 
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
        
@app.route('/')
def index():
    index =['SCIENCE',
            'SPORTS',
            'ENTERTAINMENT',
            'SOCIAL',
            'SHOOT',
            'FOOD',
            'LITERATURE'
            ]
    
    pages=[]
    for i in range(0,7):
        
        cur = g.c.execute('select * from {} order by random() limit 5'.format(index[i]))
        articles = [dict(key=row[0], title=row[1], link=row[2], link_img=row[3], abstract=row[4] ) for row in cur.fetchall()]
        pages.append(articles)
        conn_db = True
    return render_template('index.html', pages=pages,conn_db=conn_db)

if __name__ == '__main__':
    app.run()
