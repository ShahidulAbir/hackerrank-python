# Enter your code here. Read input from STDIN. Print output to STDOUT

number_of_elements_in_A = int(input())
A = set(list(map(int, input().split())))

number_of_operations = int(input())

for i in range(number_of_operations):
    operation = input().split()[0]
    B = set(list(map(int, input().split())))

    if operation == 'update':
        A.update(B)
    elif operation == 'intersection_update':
        A.intersection_update(B)
    elif operation == 'difference_update':
        A.difference_update(B)
    else:
        A.symmetric_difference_update(B)

print(sum(A))
