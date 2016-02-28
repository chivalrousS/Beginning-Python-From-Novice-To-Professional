#!/usr/bin/env python
#coding:utf-8

import sys,os,re

storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
    
def lookup(data,label,name):
    return data[label].get(name)

def store(data,*full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1,'')
        labels = 'first','middle','last'
        for label,name in zip(labels,names):
            people = lookup(data,label,name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]

if __name__ == '__main__':
    d = {}
    init(d)
    store(d,'Luke Skywalker','Anakin Skywalker')
    print lookup(d, 'last', 'Skywalker')