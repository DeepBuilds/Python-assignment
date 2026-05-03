def filehandling_operstion():
    with open("data.txt","w") as file:
        file.write("this si line one \n")
        file.write("this is line two \n")
        print("file written succesfull")
    with open("data.txt","r" ) as file:
        content=file.read()
        print(content)
    with open('data.txt','a') as file:
        file.write("this is appended line")
        print("Data appended")
    with open("data.txt","r" ) as file:
        after_content=file.read()
        print(after_content)
filehandling_operstion()