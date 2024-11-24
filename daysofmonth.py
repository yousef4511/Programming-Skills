# step 1: create a dictionary mapping month numbers to the member of days
month_days = {
    1: 31,  # January
    2: 28,  # Febuary
    3: 31,  # March
    4: 30,  # April  
    5: 31,  # May
    6: 30,  # June
    7: 31,  # july
    8: 31,  # August
    9: 30,  # September
    10: 31, # Octobar
    11: 30, # November
    12: 31  # December 
}

month = int(input("Enter the month number (1-12):"))

if 1 <= month <= 12:
    if month == 2:
        year = int(input("Is it a leap year? (Enter 1 for yes, 0 for No):"))
        if year == 1:
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days .")
    else:
        print(f"The month {month} has {month_days[month]}days.")
else:
    print("invalid month number. Please enter a number between 1 and 12.")