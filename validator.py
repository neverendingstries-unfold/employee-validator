import csv
from pathlib import Path

#BASE_DIR = Path(__file__).resolve().parent

file_path = Path("data") / "abc.csv"
try:
    with open(file_path, mode="r", newline="") as f:
        reader = csv.DictReader(f)
        print(reader.fieldnames)
        row_count = 0
    
        for row in reader:
            print(row) 
            row_count += 1
            
            
        print(f"Total rows: {row_count}")
        
except FileNotFoundError:
    print(f"File not found: {file_path}")        
        
   #when i add new empty row no count increased it has no imapct 
   #when i added a clumn whith no comma it is adding to previus header and no creashing     {'employee_id': 'EMP006', 'email': 'test@company.com15-01-23', 'hire_date': None, 'salary': None, 'role': None, 'experience': None} 

