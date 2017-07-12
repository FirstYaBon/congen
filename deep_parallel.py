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

filename_array = ['korea_short.txt','korea_short2.txt']
start_time = time.time()


for i in len(filename_array):
    lines


    
each_line = pool.map(deep, lines)

output = open("DCkorea.txt", "w", encoding='utf-8')

output.write('\n'.join(lines))

output.close()
pool.close
pool.join
print("DONE")
print("--- %s seconds ---" % (time.time() - start_time))
