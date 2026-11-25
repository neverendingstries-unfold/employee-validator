import csv
from pathlib import Path
import re
import datetime

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

def is_validate_email(email:str) -> bool:
    """Validate the email address format."""
    email_regex = r'^[a-z0-9._-]+@company\.com$'
    return re.fullmatch(email_regex, email, re.IGNORECASE) is not None
    
def is_valid_date(date_str: str) -> bool:
    """Validate the date format (DD-MM-YY)."""
    try:
        datetime.datetime.strptime(date_str, "%d-%m-%y")
        return True
    except ValueError:
        return False

def is_valid_salary(salary: str) -> bool:
    """Validate the salary format (numeric)."""
    try:
        salary_value = float(salary)
        return 118000 <= salary_value <= 120000000
    except ValueError:
        return False
def is_valid_experience(experience: str) -> bool:
    """Validate the experience format (numeric)."""
    try:
        experience_value = float(experience)
        return 0 <= experience_value <= 40
    except ValueError:
        return False    
def validate_row(row:dict, seen_ids:set) ->list[str]:
    """Validate a single row of employee data."""
    errors = []
    
    # Validate employee_id
    employee_id = row.get("employee_id")
    if not employee_id:
        errors.append("missing employee_id")
    elif employee_id in seen_ids:
        errors.append("duplicate employee_id")
    else:
        seen_ids.add(employee_id)
    #validate email
    email = row.get("email")
    if not email or not is_validate_email(email):
        errors.append("invalid email")
    #validate hire_date
    hire_date = row.get("hire_date")
    if not hire_date or not is_valid_date(hire_date):
        errors.append("invalid hire_date")
    #validate salary
    salary = row.get("salary")
    if not salary or not is_valid_salary(salary):
        errors.append("salary is not in range")
    #validate experience
    experience = row.get("experience")
    if not experience or not is_valid_experience(experience):
        errors.append("invalid experience")

    return errors

fake_row = {
    "employee_id": "EMP001", 
    "email": "bad-email", 
    "hire_date": "15-01-23", 
    "salary": "75000", 
    "role": "Engineer", 
    "experience": "5"
}
seen = set()
print(validate_row(fake_row, seen))
