# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(list(map(int, input().split())))
num_of_subsets = int(input())

flag = 1

for i in range(num_of_subsets):
    B = set(list(map(int, input().split())))
    if not (A.intersection(B) == B and A.intersection(B) != A):
        flag = 0
        break

if flag:
    print("True")
else:
    print("False")
