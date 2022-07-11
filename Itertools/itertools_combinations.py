# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

A = input().split()
string = sorted(A[0])
k = int(A[1])

for i in range(1, k + 1):
    for j in itertools.combinations(string, i):
        print("".join(j))
