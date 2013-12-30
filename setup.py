#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="kois_web",
    packages=["kois_web"],
    package_data={"kois_web": ["templates/*", "static/*"]},
    include_package_data=True,
)
