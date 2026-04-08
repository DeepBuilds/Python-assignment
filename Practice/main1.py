from temprature import celcious_to_faren as cf
from temprature import fartocelcius as fc
choice=input("Enter ")
if choice=="1":
    celcous=float(input("ENter celsi"))
    farenheight=cf.celcious_to_farhenheith(celcous)
    print("Farenheigt is ",farenheight)
else:
    farenheight=float(input("enter"))
    celcious=fc.fahrenheittocelcius(farenheight)
    print("celcuis is ",celcious)
