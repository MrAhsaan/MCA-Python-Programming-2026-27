#4. Write a Python program to accept a time duration in seconds and convert it into hours, minutes, and seconds.

time_duration = int(input("Enter time duration in Seconds: "))

hour = time_duration // 3600
rem_sec = time_duration % 3600

minute = time_duration // 60
sec = time_duration % 60

print(f"{hour} Hours: {minute} Minute: {sec} Seconds ")
