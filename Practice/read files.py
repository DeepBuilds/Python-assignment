with open("demo.txt", "r") as f:

    # Read entire file
    content = f.read()
    print(content)

    # Read specific number of characters
    f.seek(0)  # reset cursor
    print(f.read(10))

    # Read one line
    f.seek(0)
    print(f.readline())

    # Read all lines as a list
    f.seek(0)
    lines = f.readlines()
    print(lines)

    # Loop through lines
    f.seek(0)
    for line in f:
        print(line, end="")