with open("sample.txt", "w") as f:
    f.write("Python Practice 6\n")
    f.write("File handling example\n")
    f.write("Learning Python is fun\n")

print("File created and sample data written.")

with open("sample.txt", "a") as f:
    f.write("This line was appended later\n")
    f.write("Another appended line\n")

print("New lines appended to the file.")
