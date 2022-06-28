# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
a = set(list(map(int, input().split(" "))))
N = int(input())
b = set(list(map(int, input().split(" "))))

my_set = set()
my_set.update(a.difference(b))
my_set.update(b.difference(a))

my_list = list(my_set)
my_list.sort()

for item in my_list:
    print(item)
