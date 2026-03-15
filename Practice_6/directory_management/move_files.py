import shutil
import os

os.makedirs("backup_dir", exist_ok=True)

shutil.copy("sample.txt", "backup_dir/sample_copy.txt")
print("File copied to backup_dir.")

shutil.move("backup_dir/sample_copy.txt", "backup_dir/moved_sample.txt")
print("File moved and renamed.")