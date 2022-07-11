# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

A = input().split()
string = sorted(A[0])
k = int(A[1])

for i in itertools.permutations(string, k):
    print("".join(i))
