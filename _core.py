#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

class _BaseModel:
    def __init__(self, data: dict):
        if not isinstance(data, dict):
            raise TypeError
        self._data = data

    def _get(self, key): return self._data.get(key)

