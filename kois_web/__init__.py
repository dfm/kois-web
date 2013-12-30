#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

__all__ = ["app"]

import os
import flask
import sqlite3
import hashlib
from datetime import datetime

app = flask.Flask(__name__)


def connect_db():
    return sqlite3.connect(app.config["DATABASE_PATH"])


def get_db():
    db = getattr(flask.g, "_database", None)
    if db is None:
        db = flask.g._database = connect_db()
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(flask.g, "_database", None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route("/")
def index():
    kois = query_db("select * from kois order by kepoi_name")
    return flask.render_template("index.html", kois=kois)


@app.route("/cool-kois/")
def cool_kois():
    with app.open_resource("static/dressing_stars.txt", mode="r") as f:
        dressing_stars = [int(l.split()[0]) for l in f.readlines()[28:]]
    kois = query_db(("select * from kois where kepid in ({0}) "
                     "order by kepoi_name")
                    .format(",".join(map(unicode, dressing_stars))))
    return flask.render_template("index.html", kois=kois)


@app.route("/<koi_name>")
def koi(koi_name):
    return koi_name


@app.route("/submit/<koi_name>")
def submit(koi_name):
    secret = hashlib.md5(os.urandom(8)).hexdigest()
    db = get_db()
    db.cursor().execute("update kois set secret=?, submitted=? "
                        "where kepoi_name=?",
                        (secret, datetime.now(), koi_name))
    db.commit()
    return koi_name


@app.route("/finalize/<koi_name>")
def finalize(koi_name):
    db = get_db()
    db.cursor().execute("update kois set completed=? where kepoi_name=?",
                        (datetime.now(), koi_name))
    db.commit()
    return koi_name
