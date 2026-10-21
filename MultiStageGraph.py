# Multistage graph, forward approach: Algorithm FGraph(G, k, n, p)
# Vertices are numbered 1..n in order of stages; arrays are 1-indexed
# (index 0 unused) so the code matches the pseudocode line by line.

INF = float("inf")


def fgraph(c, k, n, p):
    cost = [0.0] * (n + 1)
    d = [0] * (n + 1)

    cost[n] = 0.0
    for j in range(n - 1, 0, -1):          # for j := n-1 to 1 step -1
        # Let r be a vertex such that <j, r> is an edge of G
        # and c[j, r] + cost[r] is minimum
        best_r = 0
        best = INF
        for r in range(j + 1, n + 1):
            if c[j][r] != INF and c[j][r] + cost[r] < best:
                best = c[j][r] + cost[r]
                best_r = r
        cost[j] = best                      # cost[j] := c[j,r] + cost[r]
        d[j] = best_r                       # d[j] := r

    # Find a minimum-cost path
    p[1] = 1
    p[k] = n
    for j in range(2, k):                   # for j := 2 to k-1
        p[j] = d[p[j - 1]]                  # p[j] := d[p[j-1]]

    return cost[1]


def main():
    n = int(input("Enter number of vertices n: "))
    k = int(input("Enter number of stages k: "))
    e = int(input("Enter number of edges: "))

    c = [[INF] * (n + 1) for _ in range(n + 1)]
    print("Enter each edge as: i j cost   (vertices numbered 1..n in stage order)")
    for _ in range(e):
        i, j, w = input().split()
        c[int(i)][int(j)] = float(w)

    p = [0] * (k + 1)
    total = fgraph(c, k, n, p)

    if total == INF:
        print("No path from 1 to n.")
        return
    print("Minimum cost:", total)
    print("Minimum-cost path:", " -> ".join(str(v) for v in p[1:k + 1]))


if __name__ == "__main__":
    main()