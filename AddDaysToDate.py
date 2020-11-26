'''
Code Challenge To add 'add_days' number of non-weekend days to a date and return 
the new date without using special calendar libraries, not accounting for 
holidays, and without simply looping through each day 

For fewer than five days, if it will land within the same week, just add those
days straight to it.  If it will pass through the one weekend, add on two days.

For greater than five days, it converts the number of business weeks passing
into full weeks, as the total number of days being added.  Modulus returns any
extra days that don't meet a full week. Finally, if it would end on a Sat or Sun
it pushes it out to Monday.

It helps to visualize as a matrix of integers to their corresponding days of the 
week when considering how many days are being added. It infers the ending day
of the week, which helps to calc the date in the conditional statement "if add_days <=5"
    Mon Tue Wed Thr Fri Sat Sun
    0   1   2   3   4   5   6    -> Starting day of the week to add to
    7   8   9   10  11  12  13
    14  15  16  17  18  19  20
    21  22  23  24  25  26  27

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
        #Account for one weekend's worth
        end_date = start_date + timedelta(days = (add_days + 2))

else:
    #This works for larger amount, adding more than 5 days
    calendarDaysToAdd = (add_days // 5 * 7) + (add_days % 5)
    print("Redmond's: Add", add_days,"to", start_date, "(",calendarDaysToAdd,")")

    end_date = start_date + timedelta(days = calendarDaysToAdd)
    print(end_date)
    if (end_date.weekday() == 5):
        end_date = start_date + timedelta(days = calendarDaysToAdd + 2)
    elif (end_date.weekday() == 6):
        end_date = start_date + timedelta(days = calendarDaysToAdd + 1)

print("End Date:",end_date)
