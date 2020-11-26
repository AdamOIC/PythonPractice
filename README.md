# DatesReinterpeted


A code challenge after finding some code (JavaScript run through RhinoJS) at a client site.  This challege is re-imagined for python, but could be converted for JS or others easily.

The original client code included two functions:

  function getDateAfterWorkDays(startDate, revDur) {
      var currentDate = startDate;
      var i = 0;
      console.log("Review duration is: " + revDur);
      while (i <= revDur) {
          console.log("i is at: " + i);
          console.log("Current date is: " + currentDate);
          // Skips Sunday and Saturday
          if (currentDate.getDay() !== 0 && currentDate.getDay() !== 6) {
              currentDate = addDays(currentDate, 1)
              console.log("Current date is : " + currentDate);
              i++;
          } else {
              currentDate = addDays(currentDate, 1);
              console.log("Current date is : " + currentDate);
          }
      }
      return currentDate;
  }

  function addDays(date, days) {
                  var result = new Date(date);
                  result.setDate(result.getDate() + days);
                  return result;
  }  

Example of the code being exexcuted by the client:
  var today = new Date();  
  var busDays  = getDateAfterWorkDays(today, 6)


The client framework already included special calendaring options to automatically account for business days only, which is why this problem stood out to me.  The original developer didn't use the calendaring available for dealing with business days, and instead made functions to loop through each date.  Not only that, they logged each iteration, leaving that logging in the final code.  In practice, that application works fine for short periods. In larger applications, like adding 300 days, the system would be iterating through and logging each loop.  A little unweildy.

Eventually, what drew the clients attention to a problem was that they were emailing out the final date to customers, using this code to send a date:
  var newDate = (busDate.getMonth() + 1) + ”/” + (busDate.getDate() - 1)  + “/” + (busDate.getYear() + 1900);
The main problem with that line, is a javascript.getDate() returns an integer between 1 and 31, not a zero based index.  So they were sending out dates that looked like this: "12/0/2020".


This was just a fun practice/challenge to try and apply the same concept of adding days to a date, meeting the spirit of what this client was trying to do.

It's 'vanilla' in that it doesn't use any special calendar libraries, doesn't deal with holidays, and doesn't simply loop through every day.  

Holidays could be added with a mapping of holiday/dates, comparing the date of the holiday to the starting and returned date, adding additional days to account for the holiday.
