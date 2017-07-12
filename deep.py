#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 23:18:35 2017

@author: essz
"""

import deepcut
import time
def deep(list):
    z =deepcut.tokenize(list)
    text = ' '.join(z)
    return text

def read_lines(filename):
    return open(filename,encoding='utf-8').read().split('\n')[:-1]

FILENAME = 'korea_short.txt'
lines = read_lines(filename=FILENAME)
start_time = time.time()
lines = [deep(line) for line in lines]

output = open("DCkorea.txt", "w", encoding='utf-8')

output.write('\n'.join(lines))

output.close()
print("DONE")
print("--- %s seconds ---" % (time.time() - start_time))
