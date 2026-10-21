import sys

# Sum of Subsets (backtracking), following Algorithm SumOfSub(s, k, r).
# Arrays are 1-indexed: index 0 is unused so the code matches the pseudocode.

def sum_of_sub(s, k, r, w, x, m, n, solutions):
    # Generate left child. Note: s + w[k] <= m since B_{k-1} is true.
    x[k] = 1
    if s + w[k] == m:
        # Subset found; x[k+1..n] are zero by construction
        solutions.append(x[1:k + 1] + [0] * (n - k))
        # There is no recursive call here as w[j] > 0, 1 <= j <= n.
    elif s + w[k] + w[k + 1] <= m:
        sum_of_sub(s + w[k], k + 1, r - w[k], w, x, m, n, solutions)

    # Generate right child and evaluate B_k.
    if (s + r - w[k] >= m) and (s + w[k + 1] <= m):
        x[k] = 0
        sum_of_sub(s, k + 1, r - w[k], w, x, m, n, solutions)


def main():
    n = int(input("Enter number of elements n: "))
    values = list(map(int, input(f"Enter {n} positive weights (space separated): ").split()))
    if len(values) != n:
        sys.exit(f"Error: expected {n} weights, got {len(values)}.")
    if any(v <= 0 for v in values):
        sys.exit("Error: all weights must be positive.")
    m = int(input("Enter target sum m: "))

    values.sort()  # algorithm requires nondecreasing order
    print("Sorted weights:", values)

    # 1-indexed w with a sentinel w[n+1] so the look-ahead w[k+1] is safe at k = n
    w = [0] + values + [float("inf")]
    x = [0] * (n + 2)

    # Precondition: w[1] <= m and sum of all w[i] >= m
    total = sum(values)
    if w[1] > m or total < m:
        print("No solution exists.")
        return

    solutions = []
    sum_of_sub(0, 1, total, w, x, m, n, solutions)

    if not solutions:
        print("No subset sums to", m)
        return
    for sol in solutions:
        subset = [values[i] for i in range(n) if sol[i] == 1]
        print(f"x = {sol}  ->  subset {subset}")


if __name__ == "__main__":
    main()