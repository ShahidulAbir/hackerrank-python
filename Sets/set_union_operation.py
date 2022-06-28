# Enter your code here. Read input from STDIN. Print output to STDOUT

num_English_newspaper = int(input())
rolls_English_newspaper = set(list(map(int, input().split())))
num_French_newspaper = int(input())
rolls_French_newspaper = set(list(map(int, input().split())))

print(len(rolls_English_newspaper | rolls_French_newspaper))
