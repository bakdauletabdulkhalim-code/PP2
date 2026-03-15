601
# n = int(input())
# m = list(map(int, input().split()))
# counter = 0
# for i in m:
#     squares = i**2
#     counter += squares
# print(counter)
602
# n = int(input())
# m = list(map(int, input().split()))
# counter = 0
# for i in m:
#     if i % 2 == 0:
#         counter += 1
# print(counter)
603
# n = int(input())
# m = input()
# words = m.split()
# for i,word in enumerate(words):
#     print(f"{i}:{word}", end = " ")
604
# n = int(input())
# l = list(map(int, input().split()))
# r = list(map(int, input().split()))
# d = 0
# for i,j in zip(l, r):
#     d += i*j
# print(d)
605
# n = input()
# ans = False
# for i in n:
#     if i == "A" or i == "a" or i == "E" or i == "e" or i == "I" or i == "i" or i == "O" or  i == "o" or i == "U" or i == "u":
#         ans = True
#         break
# if ans:
#     print("Yes")
# else:
#     print("No")
606
# n = int(input())
# m = list(map(int, input().split()))
# for i in m:
#     if i < 0:
#         print("No")
#         break
# else:
#     print("Yes")
607
# n = int(input())
# m = input()
# words = m.split()
# longest = max(words, key=len)
# print(longest)
608
# n = int(input())
# m = list(map(int, input().split()))
# b = sorted(set(m))
# print(*b)
609
# n = int(input())
# l = input().split()
# r = input().split()
# d = dict(zip(l, r))
# q = input()
# print(d.get(q, "Not found"))
610
# n = int(input())
# m = list(map(int, input().split()))
# counter = []
# for i in m:
#     if i != 0:
#         counter.append(i)
# print(len(counter))
# mysal1
# n = int(input())
# for i in range(1, n+1):
#     print(i*i, end = " ")
# mysal2
# n = input().split()
# counter = 0
# for i in n:
#     if len(i) == 3:
#         counter += 1
# print(counter)
# mysal3
# n = int(input())
# m = list(map(int, input().split()))
# counter = 0
# avg = sum(m)//len(m)
# for i in m:
#     if i > avg:
#         counter += 1
# print(counter)
# example1
# n = int(input())
# m = list(map(int, input().split()))
# counter = []
# for i in m:
#     if i % 2 == 0:
#         counter.append(i)
# print(*counter)
# example2
# n = input()
# words = n.split()
# r = max(words, key=len)
# print(r)
# example3
# p = int(input())
# n = input().split()
# m = input().split()
# d = dict(zip(n, m))
# q = input()
# print(d.get(q, "Not found"))
# esep1
# n = int(input())
# m = list(map(int, input().split()))
# counter = []
# for i in m:
#     if i % 2 == 0:
#         counter.append(i)
# print(sum(counter))
# esep2
# n = input().split()
# r = max(n, key=len)
# print(len(r))
# esep3
# n = int(input())
# keys = input().split()
# values = input().split()
# d = dict(zip(keys, values))
# q = input()
# print(d.get(q, "Not found"))

