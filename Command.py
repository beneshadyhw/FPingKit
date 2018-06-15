#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/7 11:12
# @Author : Aries
# @Site : 
# @File : playground.py
# @Software: PyCharm
import commands
import os
from Tkinter import *

# cmd = 'psping -i 0.2 -n 10 -q 139.159.230.43'

# -i intercept
# -n number
# -l size
# -q quite or not
# host
def parseCmd(keydict, host):
    cmd = 'fping '
    cmd += host
    for k,v in keydict.items():
        # if k == 'q':
        #     cmd += v*'-q '
        #     continue
        cmd += ' -{} {}'.format(k, str(v))

    # print cmd
    return cmd

def execCmd(cmd):
  r = os.popen(cmd)
  text = r.read()
  r.close()
  return text
# write "data" to file-filename
def writeFile(filename, data):
  f = open(filename, "w")
  f.write(data)
  f.close()

if __name__ =='__main__':
    k = {'t': 2, 'n': 10, 's': 32}
    cmd = parseCmd(k, '139.159.230.43')
    print cmd
    result = execCmd(cmd)
    writeFile('testerr.txt', result)