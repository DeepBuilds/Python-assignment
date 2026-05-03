# ===================== LIST =====================
print("=== LIST OPERATIONS ===")
lst = [1, 2, 3, 4]

# Access
print(lst[0], lst[-1])

# Update
lst[1] = 20

# Add
lst.append(5)
lst.insert(2, 99)

# Remove
lst.remove(3)        # removes value
popped = lst.pop()   # removes last
del lst[0]           # removes by index

# Other operations
print(len(lst))
print(lst.count(20))
lst.sort()
lst.reverse()

# Iteration
for x in lst:
    print(x)

print(lst)


# ===================== TUPLE =====================
print("\n=== TUPLE OPERATIONS ===")
tup = (10, 20, 30, 40)

# Access
print(tup[0], tup[-1])

# Tuple is immutable → cannot update directly

# Operations
print(len(tup))
print(tup.count(20))
print(tup.index(30))

# Iteration
for x in tup:
    print(x)

# Conversion (workaround for modification)
temp = list(tup)
temp.append(50)
tup = tuple(temp)
print(tup)


# ===================== SET =====================
print("\n=== SET OPERATIONS ===")
st = {1, 2, 3, 4}

# Add
st.add(5)
st.update([6, 7])

# Remove
st.remove(2)     # error if not present
st.discard(10)   # no error
popped = st.pop()

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

# Iteration
for x in st:
    print(x)

print(st)


# ===================== DICTIONARY =====================
print("\n=== DICTIONARY OPERATIONS ===")
d = {"a": 1, "b": 2, "c": 3}

# Access
print(d["a"])
print(d.get("x", "Not Found"))

# Add / Update
d["d"] = 4
d.update({"a": 10})

# Remove
d.pop("b")
del d["c"]

# Keys, values, items
print(d.keys())
print(d.values())
print(d.items())

# Iteration
for k, v in d.items():
    print(k, v)

# Other operations
print(len(d))
print("a" in d)

print(d)