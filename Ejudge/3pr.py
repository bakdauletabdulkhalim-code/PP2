301
# n = input()
# is_valid = True
# for i in n:
#     if int(i) % 2 != 0:
#         is_valid = False
#         break
# if is_valid:
#     print("Valid")
# else:
#     print("Not valid")
302
# n = int(input())
# while n % 2 == 0:
#     n//=2
# while n % 3 == 0:
#     n//=3
# while n % 5 == 0:
#     n//=5
# if n == 1:
#     print("Yes")
# else:
#     print("No")
303
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
304
# class hello:
#     def __init__(self, s1):
#         self.s1 = s1
#     def introduce(self):
#         print(self.s1.upper())
        
# s1 = hello(input())
# s1.introduce()
305
# class square:
#     def __init__(self, s1):
#         self.s1 = s1*s1
#     def natizhe(self):
#         print(self.s1)
# s1 = square(int(input()))
# s1.natizhe()
306
# class kobeitu:
#     def __init__(self, s1, s2):
#         self.s1 = s1*s2
#     def natizhe(self):
#         print(self.s1)
        
# s1, s2 = map(int, input().split())
# obj = kobeitu(s1, s2)
# obj.natizhe()
307
# class three:
#     def __init__(self, a, b, c, d, e, f):
#         self.a = (a, b)
#         self.c = (c, d)
#         self.e = ((e-c)**2+(f-d)**2)**0.5
#     def natizhe(self):
#         print(self.a)
#         print(self.c)
#         print(f"{self.e:.2f}")
# a, b = map(int, input().split())
# c, d = map(int, input().split())
# e, f = map(int, input().split())
# obj = three(a, b, c, d, e, f)
# obj.natizhe()
308
# example1
# n, m = map(int, input().split())
# if n > m:
#     print(m)
# if n < m:
#     print("Insufficient funds")
# if n == m:
#     print("equal")
# example2
# class salus:
#     def __init__(self, n, m):
#         if n > m:
#             self.n = m
#         if n < m:
#             self.n = "Insufficient funds"
#         if n == m:
#             self.n = "equal"
#     def natizhe(self):
#         print(self.n)
# n, m = map(int, input().split())
# obj = salus(n, m)
# obj.natizhe()
309
# class area:
#     def __init__(self, n):
#         self.n = n**2 * 3.14159
#     def natizhe(self):
#         print(f"{self.n:.2f}")
# n = area(int(input()))
# n.natizhe()
310
# class name:
#     def __init__(self, n, m):
#         self.n = n
#         self.m = m
#     def natizhe(self):
#         print(f"Student: {self.n}, GPA: {self.m}")
# n, m = input().split()
# m = float(m)
# obj = name(n, m)
# obj.natizhe()
311
# n = list(map(int, input().split()))
# a_sum = 0
# b_sum = 0
# for i in n:
#     if i % 2 == 0:
#         b_sum += i
#     if i % 2 != 0:
#         a_sum += i
# print(f"Result: {a_sum} {b_sum}")

313
# n = map(int, input().split())
# found = True 
# for m in n:
#     if m < 2:
#         continue
#     prime = True
#     for i in range(2, m):
#         if m % i == 0:
#             prime = False
#             break
#     if prime:
#         print(m, end = " ")
#         found = True
# if not found:
#     print("Not primes")  
313
# n = map(int, input().split())
# found = True
# for i in n:
#     if i < 2:
#         continue
#     prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             prime = False
#             break
#     if prime:
#         print(i)
# if not found:
#     print("No primes")
