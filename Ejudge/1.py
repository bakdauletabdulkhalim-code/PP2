# n = int(input())
# i = 1
# while n > i:
#     print(i, end=" ")
#     i = i * 2
p = int(input())
q = []
for i in range(p):
    q.append(input())
for s in sorted(set(q)):
    print(s, q.index(s)+1)
    
