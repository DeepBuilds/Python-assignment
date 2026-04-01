import os

# Delete a file
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
    print("File deleted.")
else:
    print("File not found.")

# Delete an empty folder
os.rmdir("myfolder")

# Delete folder and all its contents
import shutil
shutil.rmtree("myfolder")

# Check if file exists (before any operation)
print(os.path.exists("demo.txt"))  # True or False