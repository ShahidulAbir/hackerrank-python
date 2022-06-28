# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
array = list(map(int, input().split()))
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

happiness = 0

for item in array:
    if item in A:
        happiness += 1
    elif item in B:
        happiness -= 1

print(happiness)
