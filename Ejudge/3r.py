# 301
# n = input()
# valid = True
# for i in n:
#     if int(i) % 2 != 0:
#         valid = False
#         break
# if valid:
#     print("Valid")
# else:
#     print("Not valid")
# 302
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
# 303
# s = input()
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
# res = eval(s)
# ans = ""
# for i in str(res):
#     if i == "0": ans += "ZER"
#     if i == "1": ans += "ONE"
#     if i == "2": ans += "TWO"
#     if i == "3": ans += "THR"
#     if i == "4": ans += "FOU"
#     if i == "5": ans += "FIV"
#     if i == "6": ans += "SIX"
#     if i == "7": ans += "SEV"
#     if i == "8": ans += "EIG"
#     if i == "9": ans += "NIN"
# print(ans)
# 313
# m = map(int, input().split())
# found = True
# for n in m:
#     if n < 2:
#         continue
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(n, end=" ")
#         found = True
# if not found:
#     print("No primes")
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
