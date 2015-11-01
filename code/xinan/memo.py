#!/usr/bin/python

memo = {}

ipad_cost = 5;

def trials(n, m):
  if memo.has_key("%d,%d" % (m, n)):
    return memo["%d,%d" % (m, n)]
  elif n == 1:
    result = m + ipad_cost
  elif m < 1:
    result = m + ipad_cost
  else:
    result = min([1 + max(trials(n - 1, x - 1) + ipad_cost, trials(n, m - x)) for x in xrange(1, m + 1)])
  memo["%d,%d" % (m, n)] = result
  return result

print trials(2, 100)