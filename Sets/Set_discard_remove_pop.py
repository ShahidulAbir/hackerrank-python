n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    command_data = input().split()

    if command_data[0] == "remove":
        s.remove(int(command_data[1]))
    elif command_data[0] == "discard":
        s.discard(int(command_data[1]))
    else:
        s.pop()

print(sum(s))
