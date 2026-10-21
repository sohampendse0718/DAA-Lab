import numpy as np

# =========================
# INPUT MATRICES
# =========================

A = np.array([
    [8, 15, 6, 3],
    [13, 15, 12, 5],
    [15, 12, 16, 1],
    [7, 10, 4, 1]
])

B = np.array([
    [14, 16, 12, 20],
    [5, 16, 19, 20],
    [11, 14, 7, 15],
    [1, 6, 12, 14]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)


# =========================
# DIVIDE INTO 2x2 BLOCKS
# =========================

A11 = A[:2, :2]
A12 = A[:2, 2:]
A21 = A[2:, :2]
A22 = A[2:, 2:]

B11 = B[:2, :2]
B12 = B[:2, 2:]
B21 = B[2:, :2]
B22 = B[2:, 2:]

print("\nA11 =")
print(A11)

print("\nA12 =")
print(A12)

print("\nA21 =")
print(A21)

print("\nA22 =")
print(A22)

print("\nB11 =")
print(B11)

print("\nB12 =")
print(B12)

print("\nB21 =")
print(B21)

print("\nB22 =")
print(B22)


# =========================
# STRASSEN P, Q, R, S, T, U, V
# =========================

# P = (A11 + A22) * (B11 + B22)
P = (A11 + A22) @ (B11 + B22)

# Q = (A21 + A22) * B11
Q = (A21 + A22) @ B11

# R = A11 * (B12 - B22)
R = A11 @ (B12 - B22)

# S = A22 * (B21 - B11)
S = A22 @ (B21 - B11)

# T = (A11 + A12) * B22
T = (A11 + A12) @ B22

# U = (A21 - A11) * (B11 + B12)
U = (A21 - A11) @ (B11 + B12)

# V = (A12 - A22) * (B21 + B22)
V = (A12 - A22) @ (B21 + B22)


# =========================
# PRINT P TO V
# =========================

print("\n==============================")
print("STRASSEN CALCULATIONS")
print("==============================")

print("\nP = (A11 + A22) × (B11 + B22)")
print(P)

print("\nQ = (A21 + A22) × B11")
print(Q)

print("\nR = A11 × (B12 - B22)")
print(R)

print("\nS = A22 × (B21 - B11)")
print(S)

print("\nT = (A11 + A12) × B22")
print(T)

print("\nU = (A21 - A11) × (B11 + B12)")
print(U)

print("\nV = (A12 - A22) × (B21 + B22)")
print(V)


# =========================
# CALCULATE C1, C2, C3, C4
# =========================

C11 = P + S - T + V

C12 = R + T

C21 = Q + S

C22 = P + R - Q + U


# =========================
# PRINT C BLOCKS
# =========================

print("\n==============================")
print("C BLOCKS")
print("==============================")

print("\nC11 = P + S - T + V")
print(C11)

print("\nC12 = R + T")
print(C12)

print("\nC21 = Q + S")
print(C21)

print("\nC22 = P + R - Q + U")
print(C22)


# =========================
# COMBINE C BLOCKS
# =========================

C = np.vstack([
    np.hstack([C11, C12]),
    np.hstack([C21, C22])
])


# =========================
# FINAL MATRIX
# =========================

print("\n==============================")
print("FINAL MATRIX C = A × B")
print("==============================")

print(C)


# =========================
# NORMAL MULTIPLICATION
# FOR VERIFICATION
# =========================

normal_C = A @ B

print("\n==============================")
print("NORMAL MULTIPLICATION")
print("==============================")

print(normal_C)

print("\n==============================")
print("VERIFICATION")
print("==============================")

if np.array_equal(C, normal_C):
    print("Strassen result = Normal result")
    print("Correct: True")
else:
    print("Results do not match!")
    print("Correct: False")