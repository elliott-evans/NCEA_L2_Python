total_hours = 0
HOURLY_RATE = 18
for i in range(0,7):
    day_hours = int(input("How many hours did you work on Day {}?:  ".format(i+1)))
    total_hours += day_hours
print("This week, you worked for {:.2f} hours and earned ${}.".format(total_hours, total_hours * HOURLY_RATE)) 
