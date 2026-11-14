from datetime import datetime

# Employee Leave Database
employees = {
    "E101": {
        "Casual": 12,
        "Sick": 10,
        "Earned": 15
    }
}


# Function to display leave balance
def view_balance(emp_id):
    if emp_id not in employees:
        print("Invalid Employee ID.")
        return

    print("\n----- Leave Balance -----")
    for leave_type, balance in employees[emp_id].items():
        print(f"{leave_type}: {balance} days")


# Function to calculate leave days
def calculate_days(from_date, to_date):
    try:
        start = datetime.strptime(from_date, "%Y-%m-%d")
        end = datetime.strptime(to_date, "%Y-%m-%d")

        # Validate date order
        if end < start:
            return None

        # Count both start and end dates
        days = (end - start).days + 1
        return days

    except ValueError:
        return None


# Function to apply for leave
def apply_leave():
    emp_id = input("Enter Employee ID: ").upper()

    if emp_id not in employees:
        print("Invalid Employee ID.")
        return

    leave_type = input(
        "Enter Leave Type (Casual/Sick/Earned): "
    ).capitalize()

    if leave_type not in employees[emp_id]:
        print("Invalid Leave Type.")
        return

    from_date = input("Enter From Date (YYYY-MM-DD): ")
    to_date = input("Enter To Date (YYYY-MM-DD): ")

    days = calculate_days(from_date, to_date)

    if days is None:
        print("Invalid dates. To-date cannot be before from-date.")
        return

    available = employees[emp_id][leave_type]

    # Check leave balance
    if days <= available:

        employees[emp_id][leave_type] -= days

        print(
            f"\nLeave approved: {days} days "
            f"{leave_type} | "
            f"Balance {leave_type}: "
            f"{employees[emp_id][leave_type]}"
        )

    else:
        print(
            f"\nLeave rejected. Requested: {days} days "
            f"| Available: {available} days"
        )


# Main Menu
def main():

    while True:

        print("\n==============================")
        print(" EMPLOYEE LEAVE MANAGEMENT ")
        print("==============================")

        print("1. Apply for Leave")
        print("2. View Leave Balance")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            apply_leave()

        elif choice == "2":
            emp_id = input("Enter Employee ID: ").upper()
            view_balance(emp_id)

        elif choice == "3":
            print("Thank you for using Leave Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()