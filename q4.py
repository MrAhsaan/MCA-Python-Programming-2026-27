#4. Write a Python program to accept a time duration in seconds and convert it into hours, minutes, and seconds.

time_duration = int(input("Enter time duration in Seconds: "))

Minutes = (time_duration / 60)
Hours = (time_duration /  3600)

print("Minutes: ",Minutes)
print("Hours: ",Hours)