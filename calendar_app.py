import calendar

def display_calendar():
    print("=== Simple Calendar App ===")
    
    try:
        year = int(input("Enter year (e.g. 2025): "))
        month = int(input("Enter month (1-12): "))
        
        if 1 <= month <= 12:
            print("\nHere is the calendar:\n")
            print(calendar.month(year, month))
        else:
            print("Invalid month. Please enter a value between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    display_calendar()
