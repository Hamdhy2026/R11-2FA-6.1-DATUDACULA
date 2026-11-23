import datetime

first_name = input("Enter student first name: ").strip().title()
last_name = input("Enter student last name: ").strip().title()
section = input("Enter section: ").strip().upper()
event_name = input("Enter event name: ").strip().title()
year = int(input("Enter event year: "))
month = int(input("Enter event month: "))
day = int(input("Enter event day: "))

full_name = first_name + " " + last_name
event_date = datetime.date(year, month, day)
formatted_date = event_date.strftime("%B") + " " + str(event_date.day) + ", " + str(event_date.year)

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section)
print("Event:", event_name)
print("Event Date:", formatted_date)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("Registration record created successfully.")