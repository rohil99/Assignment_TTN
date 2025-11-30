# Ques 1

from datetime import datetime, timedelta, date
import os

original_date = datetime(2020, 3, 22, 10, 0)
print("Original date and time:", original_date)

new_date = original_date + timedelta(weeks=1, hours=12)
print("New date and time:", new_date)


# Ques 2

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


# Ques 3

cwd = os.getcwd()
print("Current working directory:", cwd)

os.makedirs("test", exist_ok=True)

print("Files and folders in CWD:", os.listdir(cwd))

os.rmdir("test")
print("Folder 'test' removed")


# Ques 4

os.rename("Assignment_week2/old_name.txt", "Assignment_week2/new_name.txt")
print("File renamed successfully")


# Ques 5

file_size = os.path.getsize("Assignment_week2/example.txt")
print(f"Size of 'example.txt': {file_size} bytes")

# Ques 6

date_str = "Feb 25 2020 4:20PM"
date_obj = datetime.strptime(date_str, "%b %d %Y %I:%M%p")
print("Datetime object:", date_obj)


# Ques 7

date_obj = datetime(2025, 2, 25)
new_date = date_obj - timedelta(days=7)
print("New date:", new_date.date())


# Ques 8

date_obj = datetime(2020, 2, 25)
formatted_date = date_obj.strftime("%A %d %B %Y")
print("Formatted date: ",formatted_date)