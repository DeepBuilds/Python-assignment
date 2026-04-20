import csv
def count_csv_rows(file_name):
    try:
        with open(file_name,mode='r',newline='') as file:
            reader=csv.reader(file)
            row_count= sum(1 for row in reader)
            return row_count
    except FileNotFoundError:
        print(f'The file {file_name} does not exist ')
        return 0
    except Exception as e:
        print(f"There is error {e}")
        return 0
if __name__=="__main__":
    file_name=input("Enter your file name (With extension):- ")
    total_count=count_csv_rows(file_name)
    if total_count > 0:
        print(f"Total number of rows are {total_count}")