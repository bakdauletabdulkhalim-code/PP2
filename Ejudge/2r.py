# 201
# n = int(input())
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# 202
# n = int(input())
# print((n*(n+1))//2)
# 203
# n = int(input())
# m = list(map(int, input().split()))
# print(sum(m))
# 204
# n = int(input())
# m = list(map(int, input().split()))
# counter = 0
# for i in m:
#     if i > 0:
#         counter = counter + 1
# print(counter)
# 205
# a = int(input())
# while a % 2 == 0:
#     a = a // 2
# if a == 1:
#     print("YES")
# else:
#     print("NO")
# 206
# n = int(input())
# m = list(map(int, input().split()))
# max_value = max(m)
# print(max_value)
# 207
# n = int(input())
# m = list(map(int, input().split()))
# max_value = max(m)
# max_index = m.index(max_value)
# print(max_index+1)
# n = int(input())
# i = 1
# while n >= i:
    
#     print(i, end = " ")
#     i = i * 2
# 208
# n = int(input())
# m = list(map(int, input().split()))
# max_value = max(m)
# max_index = m.index(max_value)
# min_value = min(m)
# min_index = m.index(min_value)
# for i in range(n):
#     if m[i] == max_value:
#         m[i] = min_value
# print(*m)
# 210
# n = int(input())
# m = list(map(int, input().split()))
# b = sorted(m)
# print(*(b[::-1]))
# 211
# n, l, r = list(map(int, input().split()))
# a = list(map(int, input().split()))
# l -= 1
# r -= 1
# while r > l:
#     a[l], a[r] = a[r], a[l]
#     l += 1
#     r -= 1
# print(*a)
# 212
# n = int(input())
# m = list(map(int, input().split()))
# for i in range(n):
#     m[i] = m[i]*m[i]
# print(*m)
# 213
# n = int(input())

# if n <= 1:
#     print("NO")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("NO")
#             break
#     else:
#         print("YES")
# 214
# n = int(input())
# m = list(map(int, input().split()))
# max_count = 0
# answer = m[0]
# for x in range(n):
#     count = m.count(x)
#     if count > max_count:
#         answer = x
#     if count == max_count and answer > x:
#         answer = x
# print(answer)
# 215
# n = int(input())
# m = []
# for i in range(n):
#     m.append(input())
#     counter_uniq = len(set(m))
# print(counter_uniq)
# 216
# n = int(input())
# m = list(map(int, input().split()))
# k = []
# for x in m:
#     if x not in k:
#         print("YES")
#         k.append(x)
#     else:
#         print("NO")
# 214r
# n = int(input())
# m = list(map(int, input().split()))
# max_counter = 0
# answer = m[0]
# for i in range(n):
#     counter = m.count(i)
#     if counter > answer:
#         i = answer
#     if counter == answer and answer > i:
#         i = answer
# print(answer)
# 215r
# a = int(input())
# b = []
# for i in range(a):
#     b.append(input())
#     counter = len(set(b))
# print(counter)
# 216r
# n = int(input())
# m = list(map(int, input().split()))
# k = []
# for i in m:
#     if i not in k:
#         print("Yes")
#         k.append(i)
#     else:
#         print("No")
# 217
# n = int(input())
# m = []
# for i in range(n):
#     m.append(input())
# count = 0
# for num in set(m):
#     if m.count(num) == 3:
#         count += 1
# print(count)
# 218
# n = int(input())
# m = []
# for i in range(n):
#     m.append(input())
# for i in sorted(set(m)):
#     print(i, m.index(i)+1)
# # example1
# n = int(input())
# m = list(map(int, input().split()))
# count = 0
# for i in set(m):
#     if i % 2 == 0:
#         count += 1
# print(count)
# # example2
# n = int(input())
# m = input().split()
# max_word = 0
# for i in range(n):
#     count = m.count(i)
#     if count > max_word:
#         i = count
# print(count)
# # example3
# n = int(input())
# m = list(map(int, input().split()))
# max_count = 0
# answer = m[0]
# for x in range(n):
#     count = m.count(x)
#     if count > max_count:
#         answer = x
#     if count == max_count and answer > x:
#         answer = x
# print(answer)
# # example1
# n = int(input())
# mylist = list(map(int, input().split()))
# print(sorted(mylist, reverse=True)[2])

# # example2
# n = int(input())
# unique = list(map(int, input().split()))
# number = 0
# if number not in unique:
#     unique.append(number)