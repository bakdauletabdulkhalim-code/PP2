# a = int(input())
# counter = []
# for i in range(0, a+1, 2):
#         counter.append(str(i))
# print(",".join(counter))

# n = int(input())
# counter = []
# for i in range(0, n+1):
#     if i % 3 == 0 and i % 4 == 0:
#         counter.append(i)
#         print(i, end = " ")
# a, b = map(int, input().split())
# counter = []
# for i in range(a, b+1):
#     counter.append(i*i)
# for i in counter:
#     print(i)
# n = int(input())
# counter = []
# for i in range(n, -1, -1):
#     print(i)
# n = input()
# print(n[::-1])
# n = int(input())
# counter = []
# for i in range(n+1):
#     counter.append(2**i)
# print(*counter)
# n = input()
# m = int(input())
# print(n * m)
#408 
# n = int(input())
# for num in range(2, n+1):
#     is_prime = True
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end = " ")
# 410
# n = input().split()
# m = int(input())
# print(*(n*m))
# 406
# n = int(input())
# a = 0
# b = 1
# counter = []
# for i in range(n):
#     counter.append(str(a))
#     a, b = b, a + b
# print(",".join(counter))
# 403
# def divisible_numbers(n):
#     for i in range(n + 1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i

# n = int(input())

# for number in divisible_numbers(n):
#     print(number, end=" ")
# 402
# example 1
# def even_numbers(n):
#     for i in range(n+1):
#         if i % 2 == 0:
#             yield i
# n = int(input())
# counter = []
# for number in even_numbers(n):
#     counter.append(str(number))
# print(",".join(counter))
example 2
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())

first = True
for num in even_numbers(n):
    if not first:
        print(",", end="")
    print(num, end="")
    first = False
    