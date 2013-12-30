#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import os
import sqlite3

with sqlite3.connect(os.path.join("kois_web", "static", "kois.db")) as conn:
    c = conn.cursor()

    # Require foreign keys for references.
    c.execute("PRAGMA foreign_keys = ON")

    c.execute("""CREATE TABLE IF NOT EXISTS groups(
            id integer primary key,
            name text
        )""")

    c.execute("""CREATE TABLE IF NOT EXISTS kois(
            id integer primary key,
            group_id integer references groups(id),
            koi_name text,
            kepid integer,
            disposition text,
            koi_kepmag real,
            koi_period real,
            koi_period_err1 real,
            koi_period_err2 real,
            koi_time0bk real,
            koi_time0bk_err1 real,
            koi_time0bk_err2 real,
            koi_ror real,
            koi_ror_err1 real,
            koi_ror_err2 real,
            koi_impact real,
            koi_impact_err1 real,
            koi_impact_err2 real,
            koi_duration real,
            koi_duration_err1 real,
            koi_duration_err2 real,
            koi_steff real,
            koi_steff_err1 real,
            koi_steff_err2 real,
            submitted text,
            remote_id text,
            completed text,
            fetched text,
            plotted text,
            comments text,
            nwalkers integer,
            steps integer,
            acor_time real,
            map_fstar real,
            map_q1 real,
            map_q2 real,
            map_period real,
            map_epoch real,
            map_duration real,
            map_ror real,
            map_impact real,
            kplr_fstar real,
            kplr_fstar_err1 real,
            kplr_fstar_err1 real,
            kplr_q1 real,
            kplr_q1_err1 real,
            kplr_q1_err2 real,
            kplr_q2 real,
            kplr_q2_err1 real,
            kplr_q2_err2 real,
            kplr_period real,
            kplr_period_err1 real,
            kplr_period_err2 real,
            kplr_epoch real,
            kplr_epoch_err1 real,
            kplr_epoch_err2 real,
            kplr_duration real,
            kplr_duration_err1 real,
            kplr_duration_err2 real,
            kplr_ror real,
            kplr_ror_err1 real,
            kplr_ror_err2 real,
            kplr_impact real,
            kplr_impact_err1 real,
            kplr_impact_err2 real
        )""")
