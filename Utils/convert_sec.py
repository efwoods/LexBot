import datetime
time_unit = input("Enter the time in seconds: ")
converted_time = datetime.timedelta(seconds=float(time_unit))
print(converted_time)