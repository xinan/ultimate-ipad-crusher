#!/usr/bin/python

from math import log, floor
from scipy.misc import comb

def trials(L, N):
  H = int(log(L, 2))
  while (True):
    total = sum(comb(H, k) for k in range(0, N + 1))
    if (total >= L+1):
      return H
    H += 1
    
def costlyiPad(L, N):
  H = int(log(L, 2))
  while (True):
    total = sum(comb(H-5*k, k) for k in range(0, N + 1))
    if (total >= L+1):
      return H
    H += 1

def costlyInf(L):
  H = int(log(L, 2))
  while (True):
    total = sum(comb(H-5*k, k) for k in range(0, floor(H/5) + 1))
    if (total >= L+1):
      return H
    H += 1

def normal(N, L):
  table = [[0 for x in range(N+1)] for x in range(L+1)]
  for l in range(1, L+1):
      table[l][1] = l
      for n in range(2, N+1):
          table[l][n] = min([
              1 + max(table[x-1][n-1], table[l-x][n]) for x in range(1, l+1)
              ])
  return table[L][N]

def constCost(N, L):
  table = [[0 for x in range(N+1)] for x in range(L+1)]
  for l in range(1, L+1):
      table[l][1] = l + 5
      for n in range(2, N+1):
          table[l][n] = min([
              1 + max(table[x-1][n-1] + 5, table[l-x][n]) for x in range(1, l+1)
              ])
  return table[L][N]

def constCostInf(L):
    table = [0 for x in range(L+1)]
    for l in range(1, L+1):
        table[l] = min([max(1 + 5 + table[x-1],
                            1 + table[l-x])
                        for x in range(1, l+1)])
    return table[L]
