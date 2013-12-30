#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import sys
import kplr
import sqlite3

if len(sys.argv) != 2:
    print("Provide a database path")
    sys.exit(1)

# Get the KOI listing from the Exoplanet Archive.
client = kplr.API()
kois = client.kois(where="koi_pdisposition+like+'CANDIDATE'")

with sqlite3.connect(sys.argv[1]) as conn:
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS kois")
    c.execute("""CREATE TABLE kois(
            id integer primary key,
            kepoi_name text,
            kepid integer,
            koi_disposition text,
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
            kplr_fstar_err2 real,
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

    columns = ["kepoi_name", "kepid", "koi_disposition",
               "koi_period", "koi_period_err1", "koi_period_err2",
               "koi_time0bk", "koi_time0bk_err1", "koi_time0bk_err2",
               "koi_ror", "koi_ror_err1", "koi_ror_err2", "koi_impact",
               "koi_impact_err1", "koi_impact_err2", "koi_duration",
               "koi_duration_err1", "koi_duration_err2", "koi_steff",
               "koi_steff_err1", "koi_steff_err2"]
    c.executemany("INSERT INTO kois({0}) VALUES ({1})"
                  .format(",".join(columns),
                          ",".join(["?" for i in range(len(columns))])),
                  [map(lambda c: getattr(k, c), columns) for k in kois])
