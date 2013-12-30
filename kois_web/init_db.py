#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

__all__ = ["init_db", "load_kois"]

import kplr
from contextlib import closing


def init_db():
    from . import app, connect_db

    with closing(connect_db()) as db:
        with app.open_resource("schema.sql", mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()


def load_kois():
    from . import connect_db

    # Get the KOI listing from the Exoplanet Archive.
    client = kplr.API()
    kois = client.kois(where="koi_pdisposition+like+'CANDIDATE'")

    with closing(connect_db()) as db:
        columns = ["kepoi_name", "kepid", "koi_disposition",
                   "koi_period", "koi_period_err1", "koi_period_err2",
                   "koi_time0bk", "koi_time0bk_err1", "koi_time0bk_err2",
                   "koi_ror", "koi_ror_err1", "koi_ror_err2", "koi_impact",
                   "koi_impact_err1", "koi_impact_err2", "koi_duration",
                   "koi_duration_err1", "koi_duration_err2", "koi_steff",
                   "koi_steff_err1", "koi_steff_err2"]
        db.cursor().executemany("INSERT INTO kois({0}) VALUES ({1})"
                                .format(",".join(columns),
                                ",".join(["?" for i in range(len(columns))])),
                                [map(lambda c: getattr(k, c), columns)
                                 for k in kois])
        db.commit()
