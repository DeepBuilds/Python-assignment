try:
    x = int(input("Enter a number: ")) 
    result = 10 / x 
except (ZeroDivisionError, ValueError) as e: 
    
    print(f"An error occurred: {e}") 
else:
    print(result)
finally:
    print("Code executed successfully")
