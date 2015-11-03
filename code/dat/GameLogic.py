N = 0
L = 0
start = 0
end = 0
table = []

def makeDPTable(N, L):
    table = [[0 for x in range(N+1)] for x in range(L+1)]
    for l in range(1, L+1):
        table[l][1] = l
        for n in range(2, N+1):
            table[l][n] = min([
                 1 + max(table[x-1][n-1], # cost if iPad is crushed
                         table[l-x][n])     # cost if iPad is not crushed
                 for x in range(1, l+1)
                ])
    return table

def initGame(userN, userL):
    global N
    N = userN
    global L
    L = userL
    global start
    start = 1
    global end
    end = L
    global table
    table = makeDPTable(N,L)
    print("A new game is initialized. You have " + str(N) + " iPads and "
          + str(L) + " levels of strength.")

def crushAtLevel(level):
    if (N == 0):
        print("No iPad left to crush. You LOSE!")
        return
    if (start == end+1):
        print("Congratulations! You WIN. The iPad will  be crushed at level "
              + str(start))
    print("Player crushed iPad at level " + str(level))
    global N
    global L
    global start
    global end
    global table
    if ((level < 1) or (level > L)):
        print("Invalid level.")
        return
    elif (level < start):
        print("The iPad is unscathed.")
    elif (level > end):
        print("The iPad was crushed!")
    else:
        l = end - start + 1
        crushCost = table[level-1][N-1]
        notCrushCost = table[l-level][N]
        if (crushCost > notCrushCost):
            print("The iPad was crushed!")
            N = N-1
            end = level-1
        else:
            print("The iPad is unscathed.")
            start = level+1
    print("You have " + str(N) + " iPads left.")
    if (start == end+1):
        print("Congratulations! You WIN. The iPad will  be crushed at level "
              + str(start))
