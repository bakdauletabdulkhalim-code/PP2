with open("sample.txt", "r") as f:
    content = f.read()

print("File content:")
print(content)

print("\nReading line by line:")

with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())
