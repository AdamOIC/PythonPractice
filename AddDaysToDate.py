'''
Code Challenge To add 'add_days' number of non-weekend days to a date and return 
the new date without using special calendar libraries, not accounting for 
holidays, and without simply looping through each day 

It nicely applies a practical use for Modulus, because (the number of days to 
add + the integer of the starting day) % 7 will tell you what day of the week 
(as an int) that addition would land on. It helped to visualize as a matrix of 
integers to their corresponding days of the week:
    Mon Tue Wed Thr Fri Sat Sun
    0   1   2   3   4   5   6    -> Starting day of the week to add to
    7   8   9   10  11  12  13
    14  15  16  17  18  19  20
    21  22  23  24  25  26  27

So if the starting day is Thursday (3) and it needs to add 10 days, that would 
land on Sunday (13). But there's no matrix sitting around like the one above to 
tell us that, so we can figure it out with modulus instead:
    13 & 7 = 6
That it ends on a Sunday is important because it needs to skip weekends.  
You cannot just divide the number of days being added by 7, then multiple the 
weeks passing by 2 (sat and sun), like this:
    math.floor(10 / 7) * 2 = 2
Because it would only add 2 extra days, while we actually need to add four days
to account for [5], [6] and [12], [13].

So when a user says they need to add 10 business days to a Thursday, they 
actually need to add 14 sequential days to their starting date.

For large numbers of days being added, the more days that elapse, the more 
weekends that pass, getting the results caught up in the same problem: the 
number of days to add on keeps growing as weekends pass too.  So the process has
to be able to repeat itself to account for the weekend growth.


Variables for a user to configure:
    1) How many days to add is specified by 'add_days'
    2) What date to start from is specified by start_date, defaulting to the 
    current date. To do, let that be declarable as mm/dd/yyyy

'''

import datetime as dt
import math

#User Configurable
##################
add_days = 10
start_date = None
##################

supplement_days = 0
days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] #Just for logging

#Functions
'''
Helper to add days if the date lands on a Saturday or Sunday
Based on the integer returned for .weekday() method on a date/time
'''
def add_days_for_weekend(pDOW):
    if pDOW == 5:
        #Saturday to monday
        return 2
    elif pDOW == 6:
        #Sunday to Monday
        return 1
    else:
        return 0


#End Functions


# To do, allow start date to be declarable as mm/dd/yyyy or similar string
if start_date is None:
    sd = dt.date.today()

print("Starting Date:", sd)
c_dow = sd.weekday()
print("Starting Day of the week is: ", days_of_week[c_dow], c_dow)

full_weeks_passed = math.floor((c_dow + add_days) / 7)
print("Full weeks being added:", full_weeks_passed)
supplement_days = full_weeks_passed * 2

# If the days added will end on a sat or sun, need to make up for those days 
# because they won't be caught as part of a full week passed. The modulus of the
# total days will infer the ending day as Saturday or Sunday.
ending_dow = (c_dow + add_days) % 7
print("Based on the initial days being added, this will end on",days_of_week[ending_dow])
supplement_days = supplement_days + add_days_for_weekend(ending_dow)

print("Days added to account for weekends:",supplement_days)

#If the ending day of the week plus the number of weekend days being supplemented, 
# doesn't land on a Sat/Sun it's a weekday that will end within the same week.
if (ending_dow + supplement_days) < 5: 
    final_date = sd + dt.timedelta(days=(add_days + supplement_days))
else:
    print("Based on the ending day of week and the days being added (",ending_dow + supplement_days,")there is/are additional weekends to account for")
    
    # The whole process needs to repeat, except now to account for the quantity 
    # of 'supplement_days'. To do this, 'supplement_days' repeats the process 
    # as above, but it takes the place of 'add_days'
    # To account for this repeatable process, we need to store how many days are 
    # to be added as we go.
    
    #First store what was calculated above, probably a better way to do this
    days_2_add = []
    days_2_add.append(add_days+supplement_days)

    while (ending_dow + supplement_days) >= 5:
        #Within this loop, it acts like the initial run above. But now:
        # The c_dow becomes the ending_dow
        # and the add_days becomes the supplemental_days
       
        #Reset the ending day of week based on the current ending_dow (now the c_dow) 
        # plus the supplemental days (add_days)
        ending_dow = (ending_dow + supplement_days) % 7
        full_weeks_passed = math.floor((ending_dow + supplement_days) / 7)
        print("Next go, Full weeks being added:", full_weeks_passed)
        supplement_days = full_weeks_passed * 2
        supplement_days = supplement_days + add_days_for_weekend(ending_dow)
        print("Next go, Supplemental days to add to account for weekends:",supplement_days)

        #The next batch of days to add is calculated, push it to the array for 
        # later time-delta
        days_2_add.append(supplement_days)
        
    #Finally, perform the final calc for the date
    total_tally = 0
    for i in range(0, len(days_2_add)):
        total_tally = total_tally + days_2_add[i]
    print("Adding total number of days, accounting for weekends:", total_tally)
    final_date = sd + dt.timedelta(days=total_tally)
    
print("Final Date calculated:", final_date)
