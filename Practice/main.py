import shapes
print("Choose The shape:-\n1.circle\n2.rectangle\n3.triangle")
c=input("Enter your choices")
if c=="1":
    r=float(input("ENter ir raius"))
    print("Area is ",shapes.circle(r))
elif c=="2":
    l=float(input("ENter ir length"))
    w=float(input("ENter ir breth"))
    print("area is ",shapes.rectangle(l,w))
else:
    h=float(input("ENter ir hieht"))
    b=float(input("ENter ir basse"))
    print("area",shapes.triangle(h,b))
