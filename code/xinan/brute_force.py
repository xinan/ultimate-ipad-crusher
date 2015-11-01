#!/usr/bin/python

from math import log, floor, ceil

def make_tree(left, root, right):
  return (left, root, right)
  
def make_leave(value):
  return make_tree(None, value, None)
  
def get_left(tree):
  return tree[0]
  
def get_root(tree):
  return tree[1]
  
def get_right(tree):
  return tree[2]

def get_height(tree):
  return 0 if tree == None else max(get_height(get_left(tree)), get_height(get_right(tree))) + 1
  
def print_node(tree):
  print get_root(tree)
  
def shift_tree(tree, offset):
  if tree == None:
    return tree
  else:
    return make_tree(shift_tree(get_left(tree), offset), get_root(tree) + offset, shift_tree(get_right(tree), offset))

def trials(m, n, o):
  if n == 1:
    result = None
    for x in reversed(range(1, m + 1)):
      result = make_tree(result, x + o, None)
  elif m == 1:
    result = make_leave(m + o)
  else:
   result = reduce(lambda p, n: n if get_height(n) <= get_height(p) or p == None else p, map(lambda x: make_tree(trials(m - x, n, x + o), x + o, trials(x - 1, n - 1, o)), range(1, m + 1)), None)
  return result

result = trials(15, 4, 0)
print get_height(result)
tree = result
while tree != None:
  print_node(tree)
  tree = get_left(tree)