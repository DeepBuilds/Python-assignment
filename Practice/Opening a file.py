# Opening a file
f = open("demo.txt", "r")   # modes: r, w, a, x, rb, wb
print(f.read())
f.close()

# Better way — using 'with' (auto-closes)
with open("demo.txt", "r") as f:
    print(f.read())