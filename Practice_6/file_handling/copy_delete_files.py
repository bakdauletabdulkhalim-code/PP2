import shutil
import os

shutil.copy("sample.txt", "sample_backup.txt")
print("Backup file created: sample_backup.txt")

backup = "sample_backup.txt"

if os.path.exists(backup):
    os.remove(backup)
    print("Backup file deleted safely.")
else:
    print("File not found.")
