#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 23:18:35 2017

@author: essz
"""

import deepcut
import time
import tensorflow as tf
from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(2)

def deep(list):
    z =deepcut.tokenize(list)
    text = ' '.join(z)
    return text

def read_lines(filename):
    return open(filename,encoding='utf-8').read().split('\n')[:-1]

def run(fname):
    FILENAME = fname
    lines = read_lines(filename=FILENAME)
    start_time = time.time()
    lines = [deep(line) for line in lines]
    return lines

fname_arr = ['korea_short.txt','korea_short2.txt']
lines_arr = pool.map(run, fname_arr)

output = open("DCkorea.txt", "w", encoding='utf-8')

output.write('\n'.join(lines_arr[0]))
output.write('/n'.join(lines_arr[1]))

output.close()
print("DONE")
print("--- %s seconds ---" % (time.time() - start_time))

################
##from multiprocessing.dummy import Pool as ThreadPool
##pool = ThreadPool(2)
##x = [1,2,3,4,5]
##y = [6,7,8,9,10]
##
##def add(a):
##    return a*a
##
##ans = pool.map(add, x)
##print(ans)
