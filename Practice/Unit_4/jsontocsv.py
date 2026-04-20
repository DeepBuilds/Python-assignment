import json
import csv
def json_to_csv(json_data,csv_name):
    with open(csv_name,mode='w',newline='') as csv_file:
        writer=csv.DictWriter(csv_file,fieldnames=json_data[0].keys())
        writer.writeheader()
        writer.writerows(json_data)
        print(f"CSv file created as {csv_name}")
if __name__=="__main__":
    json_data=[
        {'name':"shriram","age":18,"gender":'M'},
        {'name':"karan","age":15,"gender":'M'},
        {'name':"marnan","age":19,"gender":'M'}
        ]
    csv_file=input("Enter CSV file :- ")
    csv_file=csv_file+".csv"
    json_to_csv(json_data,csv_file)