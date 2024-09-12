# lib/debug.py
from __init__ import CONN, CURSOR
from department import Department
import ipdb

def main():
    # Drop and create the table
    Department.drop_table()
    Department.create_table()

    # Create new departments
    payroll = Department.create("Payroll", "Building A, 5th Floor")
    print(payroll)  # Should print: <Department 1: Payroll, Building A, 5th Floor>

    hr = Department.create("Human Resources", "Building C, East Wing")
    print(hr)  # Should print: <Department 2: Human Resources, Building C, East Wing>

    # Update department
    hr.name = 'HR'
    hr.location = "Building F, 10th Floor"
    hr.update()
    print(hr)  # Should print: <Department 2: HR, Building F, 10th Floor>

    # Delete department
    print("Delete Payroll")
    payroll.delete()
    print(payroll)  # Should print: <Department 1: Payroll, Building A, 5th Floor>

    # Query database to see remaining departments
    departments = CURSOR.execute('SELECT * FROM departments').fetchall()
    print(departments)  # Should show remaining rows in the table

    ipdb.set_trace()  # Allows interactive debugging

if __name__ == "__main__":
    main()
