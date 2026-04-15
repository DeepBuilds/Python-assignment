# a calculator for calculating area of shapes by taking user input
import math
while True:
    try :
        print("Welcome to the Area Calculator!")
        print("What do u want to do. choose from following option")
        todo = int(input("Parameter = 1, Area = 2 ,Basic Athematic = 3 , Weight and BMI = 4  "))

        def calculate_parameter():
            shape = str(input("choose a shape 'square'= 1, 'rectangle'= 2, 'circle' = 3 or 'triangle'= 4: "))
            if shape == "1":
                side = float(input("enter the length of the side = "))
                para = 4 * side
                print(f"The parameter of square is {para}")
            elif shape == "3":
                radius = float(input("enter the radius ="))
                para = 2 * math.pi * radius
                print(f"The parameter of the circle is {round(para,3):,}")
            elif shape == "2":
                length = float(input("Enter the length ="))
                width = float(input("enter the width = "))
                para = 2 * (length + width)
                print(f"Parameter of the rectangle is {para}")
            elif shape == "4":
                side1 = float(input("Enter side 1 :"))
                side2 = float(input("Enter side 2 :"))
                side3 = float(input("Enter side 3 :"))
                para = side1 + side2 + side3
                print(f"Parameter of the triangle is {para}")
            else:
                print("Choose a valid option")

        def calculate_area():
            shape = str(input("choose a shape 'square'= 1, 'rectangle'= 2, 'circle' = 3 or 'triangle'= 4: "))
            if shape == "1":
                side = float(input("enter the length of the side = "))
                area = side**2
                print(f"the area of square is  {area}")
            elif shape == "3":
                radius = float(input("enter the radius ="))
                area = math.pi * (radius**2)
                print(f"The area of the circle is {round(area,3)}")
            elif shape == "2":
                length = float(input("Enter the length ="))
                width = float(input("enter the width = "))
                area = length * width
                print(f"Area of the rectangle is {area}")
            elif shape == "4":
                height = float(input("Enter the height :"))
                base = float(input("Enter the base :"))
                area = 0.5 * base * height
                print(f"Area of the triangle is {area}")
            else:
                print("Choose a valid option")

        if todo == 1:
            calculate_parameter()
        elif todo == 2:
            calculate_area()
        else:
            print("Option not implemented yet.")


    except ValueError:
        print("Enter a valid input Motherfucker 🖕🏻 ")