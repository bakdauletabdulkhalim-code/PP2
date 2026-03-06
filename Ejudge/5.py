# 501
# import re
# text = input()
# result = re.match("Hello", text)
# if result:
#     print("Yes")
# else:
#     print("No")
# 502
# import re
# result = re.search(p, s)
# s = input()
# p = input()
# if result:
#     print("Yes")
# else:
#     print("No")
# 503
# import re
# s = input()
# p = input()
# result = re.findall(p, s)
# print(len(result))
# 506
# import re

# text = input()

# match = re.search(r'\S+@\S+\.\S+', text)

# if match:
#     print(match.group())
# else:
#     print("No email")
# 507
# import re
# s = input()
# p = input()
# r = input()
# result = re.sub(p, r, s)
# print(result)
# 508
# import re

# s = input()
# pattern = input()

# parts = re.split(pattern, s)

# print(",".join(parts))
# 510
# import re
# s = input()
# result = re.search("cat|dog", s)
# if result:
#     print("Yes")
# else:
#     print("No")
# 504
# text = input()
# numbers = []
# for ch in text:
#     if ch.isdigit():
#         numbers.append(ch)
# print(*numbers)
# 505
# import re
# text = input()
# pattern = r'^[A-Za-z].*[0-9]$'
# if re.match(pattern, text):
#     print("Yes")
# else:
#     print("No")
# 509
# text = input()
# words = text.split()
# count = 0
# for ch in words:
#     if len(ch) == 3:
#         count += 1
# print(count)
# 511
# text = input()
# counter = 0
# for ch in text:
#     if ch.isupper():
#         counter += 1
# print(counter)
# 512
# import re

# text = input()

# numbers = re.findall(r'\d{2,}', text)

# print(" ".join(numbers))
# 513
# TEXT = input()
# WORDS = TEXT.split()
# print(len(WORDS)
# )
# 514
# import re

# text = input()

# pattern = re.compile(r'^\d+$')

# if pattern.match(text):
#     print("Match")
# else:
#     print("No match")
# 515
# import re

# text = input()

# def double_digit(match):
#     digit = match.group()
#     return digit * 2

# result = re.sub(r'\d', double_digit, text)

# print(result)
# 516
# import re

# text = input()

# match = re.search(r'Name:\s*(.+),\s*Age:\s*(\d+)', text)

# if match:
#     name = match.group(1)
#     age = match.group(2)
#     print(name, age)
# 517
# import re

# text = input()

# dates = re.findall(r'\d{2}/\d{2}/\d{4}', text)

# print(len(dates))
# 518
# import re

# text = input()
# pattern = input()

# literal = re.escape(pattern)

# matches = re.findall(literal, text)

# print(len(matches))
# 519
# import re

# text = input()

# pattern = re.compile(r'\b\w+\b')

# words = pattern.findall(text)

# print(len(words))
# 1
# n = int(input())
# m = list(map(int, input().split()))
# sum = 0

# for i in m:
#     sum = sum + i*i
# print(sum)
# 2
# n = int(input())
# m = list(map(int, input().split()))
# counter = 0
# for i in m:
#     if i % 2 == 0:
#         counter += 1
# print(counter)
# 3
# n = int(input())
# m = list(map(int, input().split()))
# l = list(map(int, input().split()))
# s = 0
# for i in range(n):
#     s += m[i] * l[i]
# print(s)
# 4
# n = input()
# for i in n:
#     if i == "A" or i == "a" or i == "E" or i == "e" or i == "I" or i == "i" or i == "O" or i == "o" or i == "U" or i == "u":
#         print("Yes")
#         break
# else:
#     print("No")
# 5
n = int(input())
m = list(map(int, input().split()))
for i in m:
    if i < 0:
        print("No")
        break
else:
    print("Yes")