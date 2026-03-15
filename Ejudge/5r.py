1
# import re
# n = input()
# r = re.match("Hello", n)
# if r:
#     print("Yes")
# else:
#     print("No")
2
# import re
# n = input()
# m = input()
# r = re.search(m, n)
# if r:
#     print("Yes")
# else:
#     print("No")
3
# import re
# n = input()
# m = input()
# r = re.findall(m, n)
# print(len(r))
4
# n = input()
# counter = []
# for i in n:
#     if i.isdigit():
#         counter.append(i)
# print(*counter)
5
# import re
# n = input()
# pattern = r'^[A-Za-z].*[0-9]$'
# if re.match(pattern, n):
#     print("Yes")
# else:
#     print("No")
6
# import re
# n = input()
# match = re.search(r'\S+@\S+\.\S+', n)
# if match:
#     print(match.group())
# else:
#     print("No email")
7
# import re
# n = input()
# m = input()
# l = input()
# r = re.sub(m, l, n)
# print(r)
8
# import re
# n = input()
# m = input()
# r = re.split(m, n)
# print(",".join(r))
9
# n = input()
# words = n.split()
# counter = []
# for i in words:
#     if len(i)%3==0:
#         counter.append(i)
# print(len(counter))
10
# import re
# n = input()
# r = re.search("cat|dog", n)
# if r:
#     print("Yes")
# else:
#     print("No")
11
# n = input()
# counter = 0
# for ch in n:
#     if ch.isupper():
#         counter += 1
# print(counter)
12
# import re
# n = input()
# numbers = re.findall(r'\d{2,}', n)
# print(" ".join(numbers))
13
# n = input()
# words = n.split()
# print(len(words))
14
# import re
# n = input()
# pattern = re.compile(r'^\d+$')
# if pattern.match(n):
#     print("Match")
# else:
#     print("No match")
15
# import re
# n = input()
# def double_digit(match):
#     digit = match.group()
#     return digit*2
# result = re.sub(r'\d', double_digit, n)
# print(result)
16
# import re
# n= input()
# match = re.search(r'Name: \s*(.+), \s*Age: \s*(\d+)', n)
# if match:
#     name = match.group(1)
#     age = match.group(2)
# print(name, age)
17
# import re
# n = input()
# dates = re.findall(r"\d{2}/\d{2}/\d{4}", n)
# print(len(dates))
18
# import re
# n = input()
# pattern = input()
# literal = re.escape(pattern)
# match = re.findall(literal, n)
# print(len(match))
