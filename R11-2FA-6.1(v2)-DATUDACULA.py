first_name = input("Enter student first name: ").strip().title()
last_name = input("Enter student last name: ").strip().title()
section = input("Enter section: ").strip().upper()
event_name = input("Enter event name: ").strip().title()
year = int(input("Enter event year: "))
month = int(input("Enter event month: "))
day = int(input("Enter event day: "))

full_name = first_name + " " + last_name

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section)
print("Event:", event_name)
print("Event Date:", month, day, year)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")