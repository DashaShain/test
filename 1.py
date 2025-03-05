#1 Задача

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())

if num_1 <= num_2 and num_3 <= num_4:
    print ('\t', end='')

for j in range (num_4,num_3+1):
    print (j, '\t', end='')

print()


for i in range(num_1, num_2 + 1):
    print(i, '\t', end='')
    for j in range(num_3, num_4 + 1):
        print(i * j, '\t', end='')
    print()
