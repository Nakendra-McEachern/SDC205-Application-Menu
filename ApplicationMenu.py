from datetime import datetime

print("NakMce5302 Spreadsheet Automation Menu")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option and stores into the variable called option.
option = input("Please select an option: ")

print("Option", option, "has been selected.")
print("The current date and time is", str(datetime.now()))
