# 301
# n = input()
# Valid = True
# for i in n:
#     if int(i) % 2 != 0:
#         Valid = False
#         break
# if Valid:
#     print("Valid")
# else:
#     print("Not valid")
# 302
# n = int(input())
# a = 2
# b = 3
# c = 5
# while n % a == 0:
#     n = n // a
# while n % b == 0:
#     n = n // b
# while n % c == 0:
#     n = n // c
# if n == 1:
#     print("Yes")
# else:
#     print("No")
# 303
# s = input()

# # әріп → цифр
# s = s.replace("ZER", "0")
# s = s.replace("ONE", "1")
# s = s.replace("TWO", "2")
# s = s.replace("THR", "3")
# s = s.replace("FOU", "4")
# s = s.replace("FIV", "5")
# s = s.replace("SIX", "6")
# s = s.replace("SEV", "7")
# s = s.replace("EIG", "8")
# s = s.replace("NIN", "9")

# # есептеу
# res = eval(s)

# # цифр → әріп
# ans = ""
# for c in str(res):
#     if c == "0": ans += "ZER"
#     elif c == "1": ans += "ONE"
#     elif c == "2": ans += "TWO"
#     elif c == "3": ans += "THR"
#     elif c == "4": ans += "FOU"
#     elif c == "5": ans += "FIV"
#     elif c == "6": ans += "SIX"
#     elif c == "7": ans += "SEV"
#     elif c == "8": ans += "EIG"
#     elif c == "9": ans += "NIN"
# print(ans)
# 307
# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# x3, y3 = map(int, input().split())
# dist = ((x3 - x2)**2 + (y3 - y2)**2) ** 0.5
# print((x1,y1))
# print((x2,y2))
# print(f"{dist:.2f}")
# Example
# m = map(int, input().split())
# sum1 = []
# sum2 = []
# for i in m:
#     if int(i) % 2 != 0:
#         sum1.append(i)
#     if int(i) % 2 == 0:
#         sum2.append(i)
# print((sum1), (sum2))
# 311
# a = list(map(int, input().split()))
# s1 = sum(a[::2])
# s2 = sum(a[1::2])
# print(f"Result: {s1} {s2}")

# n = list(map(int, input().split()))
# for i in n:
#     if i < 2:
#         continue
#     is_prime = True
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(i, end = " ")
# if not is_prime:
#     print("No primes")
# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# list1 = list(map(int, input().split()))
# list2 = list(filter(lambda x: is_prime(x), list1))
# print(*list2)  # [2, 5, 13, 103]
# n =input()
# n = n.replace("ZER", "0")
# n = n.replace("ONE", "1")
# n = n.replace("TWO", "2")
# n = n.replace("THR", "3")
# n = n.replace("FOU", "4")
# n = n.replace("FIV", "5")
# n = n.replace("SIX", "6")
# n = n.replace("SEV", "7")
# n = n.replace("EIG", "8")
# n = n.replace("NIN", "9")

# res = eval(n)
# ans= ""
# for c in str(res):
#     if c == "0":
#         ans += "ZER"
#     if c == "1":
#         ans += "ONE"
#     if c == "2":
#         ans += "TWO"
#     if c == "3":
#         ans += "THR"
#     if c == "4":
#         ans += "FOU"
#     if c == "5":
#         ans += "FIV"
#     if c == "6":
#         ans += "SIX"
#     if c == "7":
#         ans += "SEV"
#     if c == "8":
#         ans += "EIG"
#     if c == "9":
#         ans += "NIN"
# print(ans)
# n = int(input())
# while n % 2 == 0:
#     n //= 2
# while n % 3 == 0:
#     n //= 3
# while n % 5 == 0:
#     n //= 5
# if n == 1:
#     print("Yes")
# else:
#     print("No")
# n = input()
# print(n.upper())
# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# x3, y3 = map(int, input().split())
# dist = ((x3-x2)**2+(y3-y2)**2)**0.5
# print((x1, y1))
# print((x2, y2))
# print(f"{dist:.2f}")
n, m = map(int, input().split())
if n < m:
    print(m - n)
if n == m:
    print(n - m)
else:
    print("Insufficient Funds")
    