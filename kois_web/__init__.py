#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

__all__ = ["app"]

import flask
import sqlite3

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "Hello"


@app.route("/<koi_name>")
def koi(koi_name):
    return koi_name
