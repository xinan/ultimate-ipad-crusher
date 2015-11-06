#!/usr/bin/python

from math import log, floor
from scipy.misc import comb

def combNormal(N, L):
  H = int(log(L, 2))
  while (True):
    total = sum(comb(H, k) for k in range(0, N + 1))
    if (total >= L+1):
      return H
    H += 1

def testComb(N, L):
  table = [[trials(l+1, n+1) for n in range(N)] for l in range(L)]
  return table[L-1][N-1]

def combConstCost(N, L):
  H = int(log(L, 2))
  while (True):
    total = sum(comb(H-5*k, k) for k in range(0, N + 1))
    if (total >= L+1):
      return H
    H += 1

def combConstCostInf(L):
  H = int(log(L, 2))
  while (True):
    total = sum(comb(H-5*k, k) for k in range(0, floor(H/5) + 1))
    if (total >= L+1):
      return H
    H += 1

def combDynamicCost(N, L, costFun):
  S = [0 for x in range(N+1)]
  for i in range(1, N+1):
    S[i] = S[i-1] + costFun(i)
  H = int(log(L, 2))
  while (True):
    total = sum(comb(H-S[k], k) for k in range(0, N + 1))
    if (total >= L+1):
      return H
    H += 1

def id(x):
  return x

def const5(x):
  return 5

def combDynamicCostInf(L, costFun, numCrushed):
  memory = {0: 0}
  def S(x):
    if not(x in memory):
      memory[x] = S(x-1) + costFun(x)
    return memory[x]
  H = int(log(L, 2))
  maxK = numCrushed
  while (True):
    while S(maxK+1) - S(numCrushed) < H:
      maxK = maxK +1
    total = sum(comb(H-S(k)+S(numCrushed), k) for k in range(0, maxK + 1))
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

def dynamicCost(N, L, costFunc):
  table = [[0 for x in range(N+1)] for x in range(L+1)]
  for l in range(1, L+1):
      table[l][1] = l + costFunc(N)
      for n in range(2, N+1):
          table[l][n] = min([
              1 + max(table[x-1][n-1] + costFunc(N-n+1), table[l-x][n]) for x in range(1, l+1)
              ])
  return table[L][N]

def dynamicCostInf(L, costFunc):
    table = [[0 for x in range(L+1)]]
    p = 0
    for l in range(1, L+1):
        table[p][l] = min([max(1 + costFunc(p+1) + table[x-1],
                            1 + table[p][l-x])
                        for x in range(1, l+1)])
    return table[L]
