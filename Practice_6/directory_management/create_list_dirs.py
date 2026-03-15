import os

os.makedirs("test_dir/sub_dir/example", exist_ok=True)
print("Nested directories created.")

print("\nFiles and folders in current directory:")
for item in os.listdir():
    print(item)

print("\nText files in directory:")
for file in os.listdir():
    if file.endswith(".txt"):
        print(file)