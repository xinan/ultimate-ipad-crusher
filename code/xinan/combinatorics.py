#!/usr/bin/python

from math import log
from scipy.misc import comb

def trials(N, M):
  T = int(log(N, 2))
  while (True):
    total = sum(comb(T, k) for k in xrange(0, M + 1))
    if (total >= N):
      return T
    T += 1
    
print trials(100000, 2)