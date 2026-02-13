#214 n = int(input())
# m = list(map(int, input().split()))
# max_count = 0
# answer = m[0]
# for x in m:
#     count = m.count(x)
#     if count > max_count:
#         max_count = count
#         answer = x
#     elif count == max_count and answer > x:
#         answer = x
# print(answer)
#215 n = int(input())
# a = []
# for i in range(n):
#     a.append(int(input()))
# c = len(set(a))
# print(c)
# 216n = int(input())
# a = list(map(int, input().split()))
# k = []
# for x in a:
#     if x not in k:
#         print("YES")
#         k.append(x)
#     else:
#         print("NO")
# 217n = int(input())
# a = []

# for i in range(n):
#     a.append(input())

# count = 0

# for num in set(a):
#     if a.count(num) == 3:
#         count += 1

# print(count)
# 218 n = int(input())
# a = []
# for x in range(n):
#     a.append(input())
# for x in sorted(set(a)):
#     print(x, a.index(x)+1)
# 219 
# n = int(input())
# dorama = {}

# for i in range(n):
#     name, k = input().split()
#     k = int(k)

#     if name in dorama:
#         dorama[name] += k
#     else:
#         dorama[name] = k

# for name in sorted(dorama):
#     print(name, dorama[name])
# 220n = int(input())
# doc = {}
# for _ in range(n):
#     parts = input().split()
#     if parts[0] == "set":
#         key = parts[1]
#         values = parts[2]
#         doc[key] = values
#     else:
#         key = parts[1]
        
# n = int(input())
# 205if n <= 0:
#     print("NO")
# else:
#     while n % 2 == 0:
#         n //= 2
#     if n == 1:
#         print("YES")
#     else:
#         print("NO")
# 207n = int(input())
# m = list(map(int, input().split()))
# max_value = max(m)
# max_index = m.index(max_value)
# print(max_index+1)
# 208n = int(input())
# i = 1
# while n >= i:
#     print(i, end=" ")
#     i = i * 2
# 209n = int(input())
# m = list(map(int, input().split()))
# max_value = max(m)
# min_value = min(m)
# for i in range(n):
#     if m[i] == max_value:
#         m[i] = min_value
# print(*m)
# 210n = int(input())
# m = list(map(int, input().split()))
# m.sort(reverse = True)
# print(*m)
# 211n, l, r = map(int, input().split())
# a = list(map(int, input().split()))
# l -= 1
# r -= 1
# while r > l:
#     a[l], a[r] = a[r], a[l]
#     l += 1
#     r -= 1
# print(*a)
# 212n = int(input())
# m = list(map(int, input().split()))
# for i in range(n):
#     m[i] **= 2
# print(*m)
# 213n = int(input())
# if n <= 1:
#     print("No")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("No")
#             break
#     else:
#         print("Yes")
# 219n = int(input())
# dorama = {}
# for i in range(n):
#     name, k = input().split()
#     k = int(k)
#     if name in dorama:
#         dorama[name] += k
#     else:
#         dorama[name] = k
# for name in sorted(dorama):
#     print(name, dorama[name])
