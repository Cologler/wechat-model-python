#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

'''
NimbleText template:
    @property
    def <% $0.toWords().replace(/ /gm, '_').toLowerCase() %>(self):
        return self._get('$0')
'''
class _BaseModel:
    def __init__(self, data: dict):
        if not isinstance(data, dict):
            raise TypeError
        self._data = data

    def _get(self, key): return self._data.get(key)

