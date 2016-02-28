#!/usr/bin/env python
#coding:utf-8

import sys,os,re

def print_params(*para):
    print para
    
def print_params2(title,*params):
    print title
    print params
    
def print_params3(**params):
    print params
    
def print_params4(x,y,z=3,*pospar,**keypar):
    print x,y,z
    print pospar
    print keypar
    
if __name__ == '__main__':
    #print_params(1,2,3)
    #print_params2('params:',1,2,3)
    #print_params3(x = 1, y = 2, z = 3)
    print_params4(1, 2, 4,5,6,7,foo=1,bar=3)
    print_params4(1,2)