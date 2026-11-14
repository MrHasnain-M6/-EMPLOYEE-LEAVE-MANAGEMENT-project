## Employee Leave Management System

A simple command-line based Employee Leave Management System developed in Python. This project allows employees to apply for leave, check their leave balance, and automatically validates leave requests based on available leave quotas.

📌 Project Overview
        The Employee Leave Management System is designed to automate basic leave management operations within an organization.

        The system maintains employee leave records and provides functionalities such as:

        Applying for leave
        Viewing leave balance
        Leave balance validation
        Automatic leave deduction after approval
        Date range calculation
        Input validation
        This project is implemented using Python and follows a menu-driven approach.

🚀 Features
        1. Apply for Leave
             Employees can apply for different types of leaves by entering:

            Employee ID
            Leave Type
            From Date
            To Date
            The system automatically calculates the total leave days and checks availability before approval.

        2. View Leave Balance
            Employees can view their remaining leave balance for:

            Casual Leave
            Sick Leave
            Earned Leave
        3. Leave Validation
            The system validates:

            Employee ID
            Leave Type
            Date Format
            Date Range
            Invalid entries are rejected with appropriate messages.

        4. Automatic Leave Deduction
            When a leave request is approved:

            Leave balance is reduced automatically.
            Updated balance is displayed immediately.
            🛠 Technologies Used
            Python 3
            datetime Module


 📂 Project Structure
            EmployeeLeaveManagement/
            │
            ├── leave_management.py
            ├── README.md
            │
            └── requirements.txt (optional)
            🧠 Concepts Used
            This project demonstrates several important Python programming concepts.

            Dictionary Data Structure
            Employee records and leave balances are stored using nested dictionaries.

            employees = {
                "E101": {
                    "Casual": 12,
                    "Sick": 10,
                    "Earned": 15
                }
            }
        Functions
        The project is divided into reusable functions:

        Function	Purpose
        view_balance()	Displays leave balance
        calculate_days()	Calculates leave duration
        apply_leave()	Processes leave requests
        main()	Controls menu navigation
        Conditional Statements
        The system uses:

        if
        elif
        else
        for:

        Validation
        Approval decisions
        Menu selection
        Loops
        A while True loop is used to continuously display the menu until the user exits the application.

        while True:
            ...
        Exception Handling
        Date input errors are handled using:

        try:
            ...
        except ValueError:
            ...
        This prevents the application from crashing when invalid dates are entered.

        Date and Time Module
        The Python datetime module is used for:

        Date conversion
        Date validation
        Leave duration calculation
        datetime.strptime()


🔄 Project Workflow

    Start
    │
    ▼
    Display Main Menu
    │
    ├── Apply Leave
    │       │
    │       ▼
    │   Validate Employee ID
    │       │
    │       ▼
    │   Validate Leave Type
    │       │
    │       ▼
    │   Validate Dates
    │       │
    │       ▼
    │ Calculate Leave Days
    │       │
    │       ▼
    │ Check Available Balance
    │       │
    │   ┌── Yes ──► Approve Leave
    │   │             │
    │   │             ▼
    │   │      Deduct Balance
    │   │
    │   └── No ──► Reject Leave
    │
    ├── View Balance
    │       │
    │       ▼
    │   Display Balance
    │
    └── Exit
            │
            ▼
            End


📋 Leave Approval Logic
    Step 1
        User enters:

        Employee ID
        Leave Type
        From Date
        To Date
    Step 2
        System calculates:

        days = (end - start).days + 1
    Step 3
        System compares:

        Requested Days <= Available Balance
    Step 4
        Decision:

        If true → Leave Approved
        If false → Leave Rejected


💻 Sample Execution
        Apply Leave
        Enter Employee ID: E101
        Enter Leave Type (Casual/Sick/Earned): Casual
        Enter From Date (YYYY-MM-DD): 2025-08-01
        Enter To Date (YYYY-MM-DD): 2025-08-03

        Leave approved: 3 days Casual
        Balance Casual: 9
        View Balance
        Enter Employee ID: E101

        ----- Leave Balance -----
        Casual: 9 days
        Sick: 10 days
        Earned: 15 days

✅ Validation Rules
    Employee ID Validation
    The Employee ID must exist in the employee database.

    Example:

    E101
    Leave Type Validation
    Allowed values:

    Casual
    Sick
    Earned
    Date Validation
    Accepted format:

    YYYY-MM-DD
    Example:

    2025-08-15
    Date Range Validation
    The end date cannot be earlier than the start date.

    Invalid:

    From Date: 2025-08-10
    To Date: 2025-08-05


🎯 Learning Outcomes
    By building this project, developers can learn:

    Python Fundamentals
    Functions
    Dictionaries
    Loops
    Conditional Statements
    Exception Handling
    Date Manipulation
    Input Validation
    Menu-Driven Programs
    Basic Business Logic Implementation
