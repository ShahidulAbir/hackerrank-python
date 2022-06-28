# Enter your code here. Read input from STDIN. Print output to STDOUT

tests = int(input())

for i in range(tests):
    elements_in_A = int(input())
    A = set(list(map(int, input().split())))

    elements_in_B = int(input())
    B = set(list(map(int, input().split())))

    if A.intersection(B) == A:
        print("True")
    else:
        print("False")
