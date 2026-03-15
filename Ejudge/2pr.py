201
# n = int(input())
# if n % 2 == 0:
#     print("YES")
# else:
#     print("NO")
202
# n = int(input())
# counter = []
# for i in range(1,n+1):
#     if i not in counter:
#         counter.append(i)
# print(sum(counter))
203
# n = int(input())
# m = list(map(int, input().split()))
# print(sum(m))
204
# n = int(input())
# m = list(map(int, input().split()))
# counter = 0
# for i in m:
#     if i <= 0:
#         counter+=1
# print(counter)
205
# n = int(input())
# while n % 2 == 0:
#     n = n // 2
# if n == 1:
#     print("Yes")
# else:
#     print("No")
206
# n = int(input())
# m = list(map(int, input().split()))
# max_number = max(m)
# print(max_number)
207
# n = int(input())
# m = list(map(int, input().split()))
# max_number = max(m)
# max_index = m.index(max_number)
# print(max_index+1)
208
# n = int(input())
# i = 1
# while n >= i:
#     print(i, end = " ")
#     i = i * 2
209
# n = int(input())
# m = list(map(int, input().split()))
# max_number = max(m)
# min_number = min(m)
# max_index = m.index(max_number)
# for i in range(n):
#     if max_number == m[i]:
#         m[i] = min_number
#         print(*m)
210
# n = int(input())
# m = list(map(int, input().split()))
# b = sorted(m, reverse = True)
# print(b)
# 211
# n, m, l = map(int, input().split())
# a = list(map(int, input().split()))
# m -= 1
# l -= 1
# while l > m:
#     a[m], a[l] = a[l], a[m]
#     m += 1
#     l -= 1
# print(*a)
212
# n = int(input())
# m = list(map(int, input().split()))
# for i in m:
#     print(i*i, end=" ")
213 
# n = int(input())
# is_prime = True
# for i in range(2, int(n**0.5) + 1):
#     if n % i == 0:
#         is_prime = False
#         break
# if is_prime and n>1:
#     print("Yes")
# else:
#     print("No")
214
# n = int(input())
# m = list(map(int, input().split()))
# max_count = 0
# answer = m[0]
# for i in m:
#     count = m.count(i)
#     if count > max_count:
#         max_count = count
#         answer = i
#     if count == max_count and answer > i:
#         answer = i
# print(answer)
215
# n = int(input())
# m = []
# for i in range(n):
#     m.append(input())
# print(len(set(m)))
216
# n = int(input())
# m = list(map(int, input().split()))
# k = []
# for i in m:
#     if i not in k:
#         k.append(i)
#         print("YES")
#     else:
#         print("NO")
218
# n = int(input())
# m = []
# for i in range(n):
#     m.append(input())
# for i in sorted(set(m)):
#     print(i, m.index(i)+1)
205
# n = int(input())
# while n % 2 == 0:
#     n = n // 2
# if n == 1:
#     print("yes")
# else:
#     print("No")
208
# n = int(input())
# i = 1
# while n >= i:
#     print(i, end = " ")
#     i = i * 2
209
# n = int(input())
# m = list(map(int, input().split()))
# k = max(m)
# l = min(m)
# for i in range(n):
#     if m[i] == k:
#         m[i] = l
# print(*m)
210
# n = int(input())
# m = list(map(int, input().split()))
# b = sorted(set(m), reverse = True)
# print(*b)
211
# n, l, r = list(map(int, input().split()))
# a = list(map(int, input().split()))
# l -= 1
# r -= 1
# while r > l:
#     a[l], a[r] = a[r], a[l]
#     l += 1
#     r -= 1
# print(*a)
213
# n = int(input())
# prime = True
# for i in range(2, int(n**0.5)+1):
#     if n % i == 0:
#         prime = False
#         break
# if prime and n > 1:
#     print("Yes")
# else:
#     print("No")
214
# n = int(input())
# l = list(map(int, input().split()))
# m = 0
# ans = l[0]
# for i in l:
#     c = l.count(i)
#     if c > m:
#         ans = i
#         m = c
#     if m == c and ans > i:
#         ans = i
# print(ans)
215
# n = int(input())
# m = []
# for i in range(n):
#     m.append(input())
# print(len(set(m)))
216 
# n = int(input())
# m = list(map(int, input().split()))
# k = []
# for i in m:
#     if i not in k:
#         k.append(i)
#         print("Yes")
#     else:
#         print("No")
217
# n = int(input())
# m = []
# for i in range(n):
#     m.append(input())
# count = 0
# for j in set(m):
#     if m.count(j) == 3:
#         count += 1
# print(count)
218
# n = int(input())
# m = []
# for i in range(n):
#     m.append(input())
# for i in sorted(set(m)):
#     print(i, m.index(i)+1)