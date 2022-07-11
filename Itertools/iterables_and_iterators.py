# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

length = int(input())
array = input().split()
sub_length = int(input())

total = 0
has_a = 0


for i in itertools.combinations(array, sub_length):
    if 'a' in i:
        has_a += 1
    total += 1

print(has_a / total)
