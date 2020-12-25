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

import datetime as dt
import re

#Functions
def datestr2dateobj(date_str, delim):
    '''Take a string formatted date and turn it into a datetime object
        The string should be mm dd yyyy, with delim identifying - or /'''
    str_format = "%m/%d/%Y"
    if delim == "-":
        str_format = "%m-%d-%Y"

    try:
        return dt.datetime.strptime(date_str, str_format)

    except(ValueError):
        print("The date entered is not correct, please try again")
        return False


def identify_date_str(date_str):
    '''#function to figure out what date format they entered mm/dd/yyyy or
     mm-dd-yyyy '''
    fs, ds = "/", "-"

    #narrow it down by the delimiter user entered then match a pattern
    if fs in date_str:
        #mm/dd/yyyy
        pattern = r'\d{1,2}/\d{1,2}/\d{4}'
        res = re.search(pattern, date_str)
        if res is not None:
            return datestr2dateobj(date_str, fs)

    elif ds in date_str:
        #mm-dd-yyyy
        pattern = r'\d{1,2}-\d{1,2}-\d{4}'
        res = re.search(pattern, date_str)
        if res is not None:
            return datestr2dateobj(date_str, ds)

    else:
        #no match
        print("Enter the date as a month, day, and four digit year using a ")
        print("dash '-' or forward slash '/'")
        return False


#End Functions


start_date = None

#To default to today
#if start_date is None:
#   start_date = dt.date.today()

#For user entered and code validated date
while start_date is None or start_date is False:
    start_date = identify_date_str(input("Enter starting date as mm/dd/yyyy or mm-dd-yyyy: "))

#Number of Days to Add to a valid date
add_days = None
while add_days is None:
    try:
        add_days = int(input("Enter number of weekdays to add: "))
    except(ValueError):
        print("\nEnter a whole number (ex. 5, 69)")
        add_days = None

#Process return value
if add_days <= 5:
    if (start_date.weekday() + add_days) < 5: 
        #the number of days being added will be within the same business week
        end_date = start_date + dt.timedelta(days = add_days)
    else:
        #it would end on a Saturday or goes through the full weekend
        end_date = start_date + dt.timedelta(days = (add_days + 2))

else:
    #This adds on for larger amounts of days, by considering the passing of
    # "business" weeks by Charles
    calendarDaysToAdd = (add_days // 5 * 7) + (add_days % 5)
    print("Add", add_days,"to", start_date, "(",calendarDaysToAdd,")")

    end_date = start_date + dt.timedelta(days = calendarDaysToAdd)
    print(end_date)
    if (end_date.weekday() == 5):
        end_date = start_date + dt.timedelta(days = calendarDaysToAdd + 2)
    elif (end_date.weekday() == 6):
        end_date = start_date + dt.timedelta(days = calendarDaysToAdd + 1)

print("End Date:",end_date)
