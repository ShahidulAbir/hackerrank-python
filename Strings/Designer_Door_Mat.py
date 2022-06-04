# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split(" "))

for i in range(N):
    mid = N // 2

    if i < mid:
        print((".|." * (2 * i + 1)).center(M, "-"))
    elif i == mid:
        print("WELCOME".center(M, "-"))
    else:
        print((".|." * (2 * (N - i - 1) + 1)).center(M, "-"))
