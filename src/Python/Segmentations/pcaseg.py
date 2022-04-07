#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np


def pcaseg(data, inicBU, q, flag):
    minres = np.floor(len(data[:][0])/200).astype(int)
    degree = 1
    left_x = np.arange(0, len(data[:][0]), minres)
    right_x = left_x + minres
    right_x[len(right_x) - 1] = len(data[:][0]) - 1
    number_of_segments = len(left_x)
    segment = np.zeros(number_of_segments, dtype = [('lx', int),
                                  ('rx', int),
                                  ('mc', float),
                                  ('c', float)])
    
    for i in range(0, number_of_segments):
        segment[i]['lx'] = left_x[i]
        segment[i]['rx'] = right_x[i]
        segment[i]['mc'] = float('inf')
        segment[i]['c'] = float('inf')
    
    tc = degree
    
    return (segment, tc)

