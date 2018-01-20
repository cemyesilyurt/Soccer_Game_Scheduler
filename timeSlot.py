"""
File timeSlot.
Defines class TimeSlot.
"""
"""
Original Contributor: Cem Hasan Mehmet Yesilyurt
Last Modified: December 20, 2017
"""

import datetime
from functools import total_ordering

@total_ordering
class TimeSlot:
   """
   One object of this class represents one time slot.
   """
    
   def __init__(self, start, tDelta):
      """
      Sets start and end times and availability for this object.  start is a datetime object, tDelta is a timedelta object.
      """
      self.start = start
      self.end = start + tDelta  # makes a datetime object
      self.isAvailable = True

   def book(self):
      """
      Sets object's availability to false.
      """
      self.isAvailable = False
      
   def __str__(self):
      """
      Returns string of object.
      """
      return 'Start: ' + str(self.start) + ', End: ' + str(self.end)

   def __eq__(self, other):
      """
      Returns true if self and other are equal.
      """
      return (self.start == other.start) and (self.end == other.end)

   def __lt__(self, other):
      """
      Returns true if self starts before other.
      """
      return self.start < other.start


if __name__ == "__main__":
   
   start = datetime.datetime(2017, 3, 10, 10, 30)
   tDelta = datetime.timedelta(0, 0, 0, 0, 30, 1, 0)   
   ts = TimeSlot(start, tDelta)
   print(start)
   print(start + tDelta)
   print(ts.start)
   print(ts.end)
   print(ts)
   
   ts1 = TimeSlot(datetime.datetime(2017, 3, 10, 10, 30), datetime.timedelta(0, 0, 0, 0, 30, 1, 0))
   ts2 = TimeSlot(datetime.datetime(2017, 3, 10, 9, 00), datetime.timedelta(0, 0, 0, 0, 30, 1, 0))
   ts3 = TimeSlot(datetime.datetime(2017, 3, 17, 9, 00), datetime.timedelta(0, 0, 0, 0, 30, 1, 0))
   print(ts1 >= ts2)
   print(ts2 < ts3)