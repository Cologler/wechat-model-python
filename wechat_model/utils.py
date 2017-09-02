#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

def print_keys(dicts):
    if isinstance(dicts, dict):
        dicts = [dicts]
    print('============ start ============')
    s = set()
    for d in dicts:
        for k in d:
            s.add(k)
    for i in s:
        print(i)
    print('============ end ============')

def print_properties(dicts):
    if isinstance(dicts, dict):
        dicts = [dicts]
    print('============ start ============')
    for d in dicts:
        for k in d:
            v = d[k]
            if str is None:
                v = 'None'
            print('%s = %s' % (k, v))
    print('============ end ============')
