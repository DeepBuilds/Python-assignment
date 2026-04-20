def operation():
    with open("example.txt","w") as file:
        file.write("This is the first line of the file.\n")
        file.write("This is the 2nd line of the file.\n")
    print("New ex created and  lines added")
    with open("example.txt",mode='r') as file:
        content=file.read()
    print("The content r terminal")
    print(content)
    with open("example.txt",mode='a') as file:
        file.write("This is the 3rd line of the file.\n")
    print("New line added")
    with open("example.txt",mode="r") as file:
        updated_content=file.read()
        print(updated_content)
if __name__=="__main__":
    operation()