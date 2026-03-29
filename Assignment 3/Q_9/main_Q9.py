import shapes

choice = input("Enter shape (circle/rectangle/triangle): ")

if choice == "circle":
    r = float(input("Enter radius: "))
    print("Area:", shapes.circle_area(r))

elif choice == "rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area:", shapes.rectangle_area(l, w))

elif choice == "triangle":
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area:", shapes.triangle_area(b, h))
else:
    print("Enter a valid input!")