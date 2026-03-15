import re
n = input()
m = input()
r = re.findall(m, n)
print(len(r))