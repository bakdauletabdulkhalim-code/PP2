# A 5 -> 2 4 6 8 10
# n = int(input())
# m = list(map(int, input().split()))
# counter = 0
# for i in m:
#     if i > (sum(m)//n):
#         counter += 1
# print(counter)
# B 
# n, m = map(int, input().split())
# f = n*n + 2*n*m + m*m
# print(f)
# C 1 10 2 -> 4
# a, b, c = map(int, input().split())
# counter = 0
# for i in range(a, b):
#     if i % c == 0:
#         counter += 1
# print(counter)
# Example
# n = int(input())
# counter = 0
# for i in range(1,n+1):
#     if n % i== 0:
#         counter += 1
# print(counter)
# Example
# n = int(input())
# m = list(map(int, input().split()))
# natural = []
# for i in range(n):
#     if i > 0:
#         natural.append(i)
# if natural:
#     print(min(natural))
# else:
#     print("No natural numbers")
1
# class Person:
#     name = "Mark"
#     name1 = "Sacha"
#     age = 27
# person1 = Person()
# person2 = Person()
# print(person1.name)
# print(person2.name1)

# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# x3, y3 = map(int, input().split())
# dist1 = ((x2-x1)**2+(y2-y1)**2)**0.5
# dist2 = ((x3-x2)**2+(y3-y2)**2)**0.5
# print(dist1+dist)

# from datetime import datetime
# start = datetime.strptime(input(), "%Y-%m-%d")
# date = True
# while date:
#     try:
#         d = datetime.strptime(input(), "%Y-%m-%d")
#         print((d-start).days)
#     except:
#         break