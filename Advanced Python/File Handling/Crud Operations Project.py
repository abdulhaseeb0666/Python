from pathlib import Path

def readfileandFolder():
    path = Path('./Python/Advanced Python/File Handling/')
    items = list(path.rglob("*"))
    for i,items in enumerate(items):
        print(f"{i+1}. {items}")

def createFile():
    try:
        readfileandFolder()
        filename = input("Enter the name of the file to create: ")
        path = Path(f"./Python/Advanced Python/File Handling/{filename}")
        if not path.exists():
            path.touch()
            with open(path, "w") as f:
                f.write(input("What you wan tto write in this file?\n"))
            f.close()
            print("File created successfully")
        else:
            print("File already exists")
    except Exception as err:
        print(f"Error: {err}")

def readFile():
    try:
        readfileandFolder()
        filename = input("Enter the name of the file to read: ")
        path = Path(f"./Python/Advanced Python/File Handling/{filename}")
        if path.exists() and path.is_file():
            with open(path, "r") as f:
                print(f.read())
            f.close()
            print("File read successfully")
        else:
            print("File does not exist")
    except Exception as err:
        print(f"Error: {err}")

def updateFile():
    try:
        readfileandFolder()
        fileName = input("Enter the name of the file to update: ")
        path = Path(f"./Python/Advanced Python/File Handling/{fileName}")
        
        if path.exists() and path.is_file():
            print("1. Append to a file")
            print("2. Overwrite a file")
            print("3. Change name of a file")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                with open(path, "a") as f:
                    f.write("\n")
                    f.write(input("What you want to append to this file?\n"))
                f.close()
                print("File updated successfully")
            if choice == 2:
                with open(path, "w") as f:
                    f.write(input("What you want to write in this file?\n"))
                f.close()
                print("File updated successfully")
            if choice == 3:
                newFileName = input("Enter the new name of the file: ")
                newPath = Path(f"./Python/Advanced Python/File Handling/{newFileName}")
                path.rename(newPath)
                print("File renamed successfully")    
        else:
            print("File does not exist")
    except Exception as err:
        print(f"Error: {err}")

def deleteFile():
    try:
        readfileandFolder()
        fileName = input("Enter the name of the file to delete: ")
        path = Path(f"./Python/Advanced Python/File Handling/{fileName}")
        if path.exists() and path.is_file():
            path.unlink()
            print("File deleted successfully")
        else:
            print("File does not exist")
    except Exception as err:
        print(f"Error: {err}")

print("Press 1 for Creating a File")
print("Press 2 for Reading a File")
print("Press 3 for Updating a File")
print("Press 4 for Deleting a File")
print("Press 5 for Appending to a File")


choice = int(input("Enter your choice: "))

if choice == 1:
    createFile()
if choice == 2:
    readFile()
if choice == 3:
    updateFile()
if choice == 4:
    deleteFile()