def makeDPTable(N, L):
    table = [[0 for x in range(N+1)] for x in range(L+1)]
    for l in range(1, L+1):
        table[l][1] = l
        for n in range(2, N+1):
            table[l][n] = min([
                1 + max(table[x-1][n-1], table[l-x][n]) for x in range(1, l+1)
                ])
    return table

def chooseLevel(table, n, start, end):
    l = end-start+1
    costs = [1 + max(table[x-1][n-1], table[l-x][n])
                   for x in range(1, l+1)]
    return start + costs.index(table[l][n])

def printTable(table):
    for r in range(len(table)):
        print(table[r])
        
