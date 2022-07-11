# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

string = input()

for i, j in itertools.groupby(string):
    print("({}, {})".format(len(list(j)), i), end=" ")
