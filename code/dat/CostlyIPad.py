L = 0
start = 0
end = 0
table = []

def initGame(userN, userL):
    global L
    L = userL
    global start
    start = 1
    global end
    end = L
    global table
    table = makeDPTable(N,L)
    print("A new game is initialized. You have "
          + str(L) + " levels of strength.")

def makeDPTable(L):
    table = [0 for x in range(L+1)]
    for l in range(1, L+1):
        table[l] = min([max(5 + table[l-1],
                            1 + table[L-l])
                        for x in range(1, l+1)])
    
