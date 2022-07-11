# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

K, M = map(int, input().split())
array = []
maximum = float('-inf')

for i in range(K):
    sub = list(map(int, input().split()))
    del sub[0]
    array.append(sub)

for j in itertools.product(*array):
    number = sum([pow(k, 2) for k in j]) % M
    if number > maximum:
        maximum = number

print(maximum)
