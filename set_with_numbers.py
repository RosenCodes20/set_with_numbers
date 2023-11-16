n, m = input().split()
set1 = set()
set2 = set()

for index in range(int(n)):
    num = int(input())
    set1.add(num)

for i in range(int(m)):
    number = int(input())
    set2.add(number)

print(*set1.intersection(set2), sep = "\n")
