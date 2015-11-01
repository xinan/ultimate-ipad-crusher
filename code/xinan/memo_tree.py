#!/usr/bin/python

from math import log, ceil
import pygraphviz as PG

memo = {}

def empty_tree():
  return None
  
def is_empty_tree(tree):
  return tree == empty_tree()

def make_tree(left, root, right):
  return (left, root, right)

def make_leave(value):
  return make_tree(empty_tree(), value, empty_tree())
  
def get_left(tree):
  return tree[0]
  
def get_root(tree):
  return tree[1]
  
def get_right(tree):
  return tree[2]

def get_height(tree):
  if is_empty_tree(tree):
    return 0
  else:
    return 1 + max(get_height(get_left(tree)), get_height(get_right(tree)))

def shift_tree(tree, offset):
  if is_empty_tree(tree):
    return empty_tree()
  else:
    return make_tree(shift_tree(get_left(tree), offset),
                     get_root(tree) + offset,
                     shift_tree(get_right(tree), offset))
                    
def get_strategy(m, n):
  return get_decision_tree(m, n, 0)

def get_decision_tree(m, n, o):
  if memo.has_key("%d,%d" % (m, n)):
    return shift_tree(memo["%d,%d" % (m, n)], o);
  elif n == 1:
    result = empty_tree()
    for x in reversed(range(1, m + 1)):
      result = make_tree(result, x + o, empty_tree())
  elif m == 1:
    result = make_leave(m + o)
  else:
    candidates = map(lambda x: make_tree(get_decision_tree(m - x, n, x + o), x + o, get_decision_tree(x - 1, n - 1, o)), range(1, m + 1))
    result = reduce(lambda p, n: n if get_height(n) <= get_height(p) or is_empty_tree(p) else p, candidates, empty_tree())
  memo["%d,%d" % (m, n)] = shift_tree(result, -o)
  return result

result = get_strategy(100, 2)
print "Worst case:", get_height(result)

G = PG.AGraph(directed=False, strict=True)

def generate_graph(tree):
  if is_empty_tree(tree):
    return
  else:
    if not is_empty_tree(get_left(tree)):
      G.add_edge(str(get_root(tree)), str(get_root(get_left(tree))), color='green')
    if not is_empty_tree(get_right(tree)):
      G.add_edge(str(get_root(tree)), str(get_root(get_right(tree))), color='red')
    generate_graph(get_left(tree))
    generate_graph(get_right(tree))
    
generate_graph(result)
G.layout(prog='dot')
G.draw('tree.png')

