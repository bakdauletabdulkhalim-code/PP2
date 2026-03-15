names = ["Ali", "Dana", "Aruzhan"]
scores = [85, 90, 95]

print("Using enumerate:")
for index, name in enumerate(names):
    print(index, name)

print("\nUsing zip:")
for name, score in zip(names, scores):
    print(name, score)

numbers = [5, 2, 8, 1]
print("\nSorted numbers:", sorted(numbers))

print("Number of students:", len(names))

print("Total score:", sum(scores))