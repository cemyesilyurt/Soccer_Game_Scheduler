"""
File main.
Prepares AYSO Area 2J game schedule.
"""
"""
Original Contributor: Cem Hasan Mehmet Yesilyurt
Last Modified: December 20, 2017
"""

from area import Area
from region import Region
from division import Division
from field import Field
from team import Team
from game import Game
from timeSlot import TimeSlot
from schedule import Schedule
import datetime
import random
import copy
import csv

"""
Initialize Areas
"""
a1 = Area('2J')

"""
Initialize Regions
"""
r64 = Region('R64')
r35 = Region('R35')
r27 = Region('R27')
r256 = Region('R256')
r1631 = Region('R1631')
r1590 = Region('R1590')
regions = [r64, r35, r27, r256, r1631, r1590]

"""
Initialize Divisions
"""
u12 = Division('U12')

"""
Initialize Time Slots
"""
timeSlots = []  # will be 2D array
NUM_WEEKS = 10
NUM_GAMES_PER_DAY = 5
TS_INITIAL = datetime.datetime(2017, 3, 10, 9, 00)
TDELTA_WEEK = datetime.timedelta(7)   
TDELTA_HOURS = datetime.timedelta(0, 0, 0, 0, 30, 1, 0)   
ts_week = 0;  ts_hr = 0

# 1st dim: week, 2nd dim: hr
for i in range(0, NUM_WEEKS):
    ts_week = TS_INITIAL + i * TDELTA_WEEK
    timeSlots.append([])
    
    for j in range(0, NUM_GAMES_PER_DAY):
        ts_hr = ts_week + j * TDELTA_HOURS
        timeSlots[i].append(TimeSlot(ts_hr, TDELTA_HOURS))

# declare preferred timeSlots, depending on season (with 9 if fall, with 3 if spring)
PREFERRED_HOURS = [1,2,3,4]

"""
# Print Time Slots
for i in range(0,len(timeSlots)):
    print('Time %i:' % (i+1))
    for j in range(0,len(timeSlots[i])):
        print('    ' + str(timeSlots[i][j]))
"""

"""
Initialize Fields
"""
# Fields for U12
f1 = Field('Miller East Field',    r64,   u12, copy.deepcopy(timeSlots))
f2 = Field('McAuliffe Field',      r64,   u12, copy.deepcopy(timeSlots))
f3 = Field('Kennedy Middle Field', r35,   u12, copy.deepcopy(timeSlots))
f4 = Field('R27 Field 1',          r27,   u12, copy.deepcopy(timeSlots))
f5 = Field('Manzanita Field 1',    r256,  u12, copy.deepcopy(timeSlots))
f6 = Field('R1631 Field 1',        r1631, u12, copy.deepcopy(timeSlots))
f7 = Field('R1590 Field 1',        r1590, u12, copy.deepcopy(timeSlots))
fields = [f1, f2, f3, f4, f5, f6, f7]

# Fields for All divisions
# f1 = Field('Wilson Park Field', r64, [u10_boys, u10_girls], timeSlots)
# f2 = Field('Miller West Field', r64, [u14_boys, u14_girls], timeSlots)
# f3 = Field('Miller East Field', r64, [u12_boys, u12_girls], timeSlots)
# f4 = Field('McAuliffe Field',   r64, [u12_boys, u12_girls], timeSlots)
# f5 = Field('Meyerholz 1 Field', r64, [u8_boys, u8_girls], timeSlots)
# f6 = Field('Meyerholz 2 Field', r64, [u8_boys, u8_girls], timeSlots)
# f7 = Field('Kennedy Middle Field', r35, [u12_boys, u12_girls], timeSlots)
# f8 = Field('R27 Field 1', r27, [u12_boys, u12_girls], timeSlots)
# f9 = Field('R27 Field 2', r27, [u14_boys, u14_girls], timeSlots)
# f10 = Field('Manzanita Field 1', r256, [u12_boys, u12_girls], timeSlots)
# f11 = Field('Manzanita Field 2', r256, [u14_boys, u14_girls], timeSlots)
# f12 = Field('R1631 Field 1', r1631, [u12_boys, u12_girls], timeSlots)
# f13 = Field('R1631 Field 2', r1631, [u14_boys, u14_girls], timeSlots)
# f14 = Field('R1590 Field 1', r1590, [u12_boys, u12_girls], timeSlots)
# f15 = Field('R1590 Field 2', r1590, [u14_boys, u14_girls], timeSlots)
# fields = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15]
       
"""
Initialize Teams
"""
gtm1 = Team('Team 1', 'Girls', r64, u12, f1, NUM_WEEKS)
gtm2 = Team('Team 2', 'Girls', r64, u12, f1, NUM_WEEKS)
gtm3 = Team('Team 3', 'Girls', r64, u12, f2, NUM_WEEKS)
gtm4 = Team('Team 4', 'Girls', r64, u12, f2, NUM_WEEKS)
gtm5 = Team('Team 5', 'Girls', r35, u12, f3, NUM_WEEKS)
gtm6 = Team('Team 6', 'Girls', r35, u12, f3, NUM_WEEKS)
gtm7 = Team('Team 7', 'Girls', r27, u12, f4, NUM_WEEKS)
gtm8 = Team('Team 8', 'Girls', r27, u12, f4, NUM_WEEKS)
gtm9 = Team('Team 9', 'Girls', r256, u12, f5, NUM_WEEKS)
gtm10 = Team('Team 10', 'Girls', r256, u12, f5, NUM_WEEKS)
gtm11 = Team('Team 11', 'Girls', r1631, u12, f6, NUM_WEEKS)
gtm12 = Team('Team 12', 'Girls', r1631, u12, f6, NUM_WEEKS)
gtm13 = Team('Team 13', 'Girls', r1590, u12, f7, NUM_WEEKS)
#gtm14 = Team('Team 14', 'Girls', r1590, u12, f7, NUM_WEEKS)
gtm14 = Team('Bye', 'Girls', r1590, u12, f7, NUM_WEEKS)

gteams = [gtm1, gtm2, gtm3, gtm4, gtm5, gtm6, gtm7, gtm8, gtm9, gtm10, gtm11, gtm12, gtm13, gtm14]

btm1 = Team('Team 1', 'Boys', r64, u12, f1, NUM_WEEKS)
btm2 = Team('Team 2', 'Boys', r64, u12, f1, NUM_WEEKS)
btm3 = Team('Team 3', 'Boys', r64, u12, f2, NUM_WEEKS)
btm4 = Team('Team 4', 'Boys', r64, u12, f2, NUM_WEEKS)
btm5 = Team('Team 5', 'Boys', r35, u12, f3, NUM_WEEKS)
btm6 = Team('Team 6', 'Boys', r35, u12, f3, NUM_WEEKS)
btm7 = Team('Team 7', 'Boys', r27, u12, f4, NUM_WEEKS)
btm8 = Team('Team 8', 'Boys', r27, u12, f4, NUM_WEEKS)
btm9 = Team('Team 9', 'Boys', r256, u12, f5, NUM_WEEKS)
btm10 = Team('Team 10', 'Boys', r256, u12, f5, NUM_WEEKS)
btm11 = Team('Team 11', 'Boys', r1631, u12, f6, NUM_WEEKS)
btm12 = Team('Team 12', 'Boys', r1631, u12, f6, NUM_WEEKS)
btm13 = Team('Team 13', 'Boys', r1590, u12, f7, NUM_WEEKS)
btm14 = Team('Bye', 'Boys', r1590, u12, f7, NUM_WEEKS)
#btm14 = Team('Team 14', 'Boys', r1590, u12, f7, NUM_WEEKS)

bteams = [btm1, btm2, btm3, btm4, btm5, btm6, btm7, btm8, btm9, btm10, btm11, btm12, btm13, btm14]


"""
Initialize Schedules
"""
girls_sched = Schedule(gteams, u12, 'Girls', NUM_WEEKS, PREFERRED_HOURS)
boys_sched = Schedule(bteams, u12, 'Boys', NUM_WEEKS, PREFERRED_HOURS)

"""
Generate Schedules
"""
girls_sched.generate()
boys_sched.generate()

"""
Generate merged schedule
"""

def mergeSchedules(sched1, sched2):
    """
    Returns a merged schedule, usually of boys and girls.
    """
    if (sched1.division is not sched2.division) or (sched1.NUM_WEEKS != sched2.NUM_WEEKS) or (sched1.PREFERRED_HOURS != sched2.PREFERRED_HOURS):
        raise ValueError('Schedules to be merged do not have same division, number of weeks, or preferred hours')
    
    mergedTeams = list()
    for team in sched1.teams:
        mergedTeams.append(team)
    for team in sched2.teams:
        mergedTeams.append(team)
    
    mergedGames = list()
    for game in sched1.games:
        mergedGames.append(game)
    for game in sched2.games:
        mergedGames.append(game)    
    
    sched3 = Schedule(mergedTeams, sched1.division, 'Boys and Girls', sched1.NUM_WEEKS, sched1.PREFERRED_HOURS)
    sched3.games = mergedGames
    return sched3


# Merge boys' and girls' schedules
boys_girls_sched = mergeSchedules(girls_sched, boys_sched)

            
# -------------------- WRITING TO PRINT SCREEN -------------------- #

# print number of home and away games for each team
print(girls_sched.getStrNumHomeAway())
print(); print()
print(boys_sched.getStrNumHomeAway())
print(); print()

# print games by team 

print(girls_sched.getStrTeamsSched("GIRLS' GAMES BY TEAM:"))
print(); print()
print(boys_sched.getStrTeamsSched("BOYS' GAMES BY TEAM:"))
print(); print()

# print all games by date
print(girls_sched.getStrTimesSched("GIRLS' GAMES BY TIME:"))
print(); print()
print(boys_sched.getStrTimesSched("BOYS' GAMES BY TIME:"))
print(); print()
print(boys_girls_sched.getStrTimesSched("GIRLS' AND BOYS' GAMES BY TIME:"))

# print time slot availabilities
for field in fields:
    for week in field.timeSlots:
        for hr in week:
            print(hr.isAvailable, end = ' ')
        print()
    print()

# print team availabilities
for gtm in gteams:
    print(gtm.weekly_availability)
for btm in bteams:
    print(btm.weekly_availability)


# -------------------- WRITING TO CSV FILES -------------------- #

f = open('u12_girls_teams_schedule.csv', 'w')
f.write(girls_sched.getStrTeamsSched("U12 GIRLS' GAMES BY TEAM:"))

f = open('u12_girls_times_schedule.csv', 'w')
f.write(girls_sched.getStrTimesSched("U12 GIRLS' GAMES BY TIME:"))

f = open('u12_boys_teams_schedule.csv', 'w')
f.write(boys_sched.getStrTeamsSched("U12 BOYS' GAMES BY TEAM:"))

f = open('u12_boys_times_schedule.csv', 'w')
f.write(boys_sched.getStrTimesSched("U12 BOYS' GAMES BY TIME:"))

f = open('u12_boys_girls_times_schedule.csv', 'w')
f.write(boys_girls_sched.getStrTimesSched("U12 BOYS' AND GIRLS' GAMES BY TIME:"))