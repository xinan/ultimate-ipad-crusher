import pygraphviz as pgv

def getHeight(node):
    return node[1]

def createNode(level, left, right):
    return (level, 1 + max(getHeight(left), getHeight(right)), left, right)

def createLeafNode(level):
    return (level, 0)

def getCrushed(node):
    return node[2]

def getNotCrushed(node):
    return node[3]

def getLevel(node):
    return node[0]

def isLeaf(node):
    return getHeight(node) == 0

def drawTree(root):
    G = pgv.AGraph(directed=False, strict=True)
    def helper(node):
        G.add_node(node, label=getLevel(node))
        if not(isLeaf(node)):
            crushed = getCrushed(node)
            notCrushed = getNotCrushed(node)
            helper(notCrushed)
            helper(crushed)
            G.add_edge(node, notCrushed, label='1')
            G.add_edge(node, crushed, label='0')
    helper(root)
    G.layout(prog='dot')
    G.draw('file.png')

def solve(N, L):
    return solveHelper(0, N, L)

def solveOne(offset, L):
    if L == 0:
        return createLeafNode(offset+1)
    else:
        return createNode(offset+1, solveOne(offset, 0),
                          solveOne(offset+1, L-1))
    

# left means crushed, right means not crushed
def solveHelper(offset, N, L):
    def solveSmall(level):
        return createNode(level, solveHelper(offset, N-1, level-offset-1),
                          solveHelper(level, N, offset + L - level))
    if L == 0:
        return createLeafNode(offset+1)
    elif N == 1:
        return solveOne(offset, L)
    else:
        return min([solveSmall(level) for level in range(offset+1, offset+L+1)],
                   key=getHeight)
        
drawTree(solve(3, 10))
