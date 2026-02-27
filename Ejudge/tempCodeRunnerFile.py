n = int(input())
counter = []
if n <= 1:
    pass
else:
    for i in range(2, n):
        if n % i == 0:
            counter.append(i)
    print(counter)