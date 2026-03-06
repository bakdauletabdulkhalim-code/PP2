import re

s = input()
pattern = r"ab*"
if re.fullmatch(pattern, s):
    print("Match found")
else:
    print("No match")


s = input()
pattern = r"ab{2,3}"
if re.fullmatch(pattern, s):
    print("Match found")
else:
    print("No match")


s = input()
matches = re.findall(r"[a-z]+(_[a-z]+)+", s)
print(matches)


s = input()
matches = re.findall(r"[A-Z][a-z]*", s)
print(matches)


s = input()
pattern = r"a.*b"
if re.fullmatch(pattern, s):
    print("Match found")
else:
    print("No match")


s = input()
result = re.sub(r"[ ,\.]+", ":", s)
print(result)


s = input()
parts = s.split('_')
camel = parts[0] + ''.join(word.capitalize() for word in parts[1:])
print(camel)


s = input()
split_list = re.findall(r"[A-Z][a-z]*", s)
print(split_list)


s = input()
result = re.sub(r"([A-Z])", r" \1", s).strip()
print(result)


s = input()
snake = re.sub(r"([A-Z])", r"_\1", s).lower().lstrip("_")
print(snake)