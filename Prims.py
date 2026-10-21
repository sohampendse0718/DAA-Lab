def Prim(E, cost, n, t):

    min_edge = min(E, key=lambda e: cost[e[0]][e[1]])

    k = min_edge[0]
    l = min_edge[1]

    mincost = cost[k][l]

    t[0][0] = k
    t[0][1] = l

    near = [0] * (n + 1)

    for i in range(1, n + 1):
        if cost[i][l] < cost[i][k]:
            near[i] = l
        else:
            near[i] = k

    near[k] = 0
    near[l] = 0

    for i in range(1, n - 1):

        j = 0
        minimum = float('inf')

        for x in range(1, n + 1):
            if near[x] != 0 and cost[x][near[x]] < minimum:
                minimum = cost[x][near[x]]
                j = x

        t[i][0] = j
        t[i][1] = near[j]

        mincost = mincost + cost[j][near[j]]

        near[j] = 0

        for k in range(1, n + 1):
            if near[k] != 0 and cost[k][near[k]] > cost[k][j]:
                near[k] = j

    return mincost


# Input
n = int(input("Enter number of vertices: "))

cost = [[0] * (n + 1) for _ in range(n + 1)]

E = []

print("Enter cost matrix:")

for i in range(1, n + 1):
    row = list(map(int, input().split()))

    for j in range(1, n + 1):
        cost[i][j] = row[j - 1]

        if i < j and cost[i][j] != 0:
            E.append((i, j))

t = [[0, 0] for _ in range(n - 1)]

mincost = Prim(E, cost, n, t)

print("Edges in MST:")
for i in range(n - 1):
    print(t[i][0], "-", t[i][1])

print("Minimum cost =", mincost)    

