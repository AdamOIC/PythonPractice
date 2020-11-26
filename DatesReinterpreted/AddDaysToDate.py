'''
Code Challenge To add 'add_days' number of non-weekend days to a date and return 
the new date without using special calendar libraries, not accounting for 
holidays, and without simply looping through each day 

For fewer than five days, if it will land within the same week, just add those
days straight to it.  If it would pass through the one weekend, add on two days.

For greater than five days, it converts the number of business weeks passing
into full weeks, as the total number of days being added.  Modulus returns any
extra days that don't meet a full week. Finally, if it would end on a Sat or Sun
it pushes it out to Monday.

'''

from datetime import date, timedelta

start_date = None
#start_date = input("Enter starting date as mm/dd/yyyy or leave blank for today: "))
if start_date is None:
    start_date = date.today()

add_days= int(input("Enter number of weekdays to add: "))

if add_days <= 5:
    if (start_date.weekday() + add_days) < 5: 
        #the number of days being added will be within the same business week
        end_date = start_date + timedelta(days = add_days)
    else:
        #it would end on a Saturday or goes through the full weekend
        end_date = start_date + timedelta(days = (add_days + 2))

else:
    #This adds on for larger amounts of days, by considering the passing of
    # "business" weeks
    calendarDaysToAdd = (add_days // 5 * 7) + (add_days % 5)
    print("Redmond's: Add", add_days,"to", start_date, "(",calendarDaysToAdd,")")

    end_date = start_date + timedelta(days = calendarDaysToAdd)
    print(end_date)
    if (end_date.weekday() == 5):
        end_date = start_date + timedelta(days = calendarDaysToAdd + 2)
    elif (end_date.weekday() == 6):
        end_date = start_date + timedelta(days = calendarDaysToAdd + 1)

print("End Date:",end_date)
