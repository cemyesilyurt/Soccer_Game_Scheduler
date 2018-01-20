# AYSO_Game_Scheduler

Original Contributor: Cem H. M. Yesilyurt
Last Modification: 12/20/17

Description:

This project is a schedule maker for the AYSO (American Youth Soccer Organization), to be used when scheduling weekly Saturday games, separately for the Fall and Spring seasons.  It is stable, and may be developed further to schedule games in end-of-season tournaments.  The project is object-oriented and uses classes with lists to keep
track of variables.  The project is written in Python.

Files:

area.py
AYSO.wpr (Wing file - for development environment)
division.py
field.py
game.py
main.py
region.py
schedule.py
team.py
timeSlot.py
u12_boys_girls_times_schedule.csv
u12_boys_teams_schedule.csv
u12_boys_times_schedule.csv
u12_girls_teams_schedule.csv
u12_girls_times_schedule.csv


Usage:

- Place folder AYSO_Schedule_Maker_v3 in target directory
- Open Python development environment software (e.g. Wing)
- Start new project, set target directory to folder
- Open main.py
- Run program


Current Features:

- AYSO U12 division, girls and boys (both genders use same fields)
- ten games maximum
- about five home games per team
- about five away games per team
- order of games: alternating home and away, some doubles (home, home .. or away, away)
- one game per week per team
- games in preferred hours
- bye if odd number of teams
- writes output as comma delimited files (.csv)
- .csv files open in MS Excel in desired format


Desired Features for the Future:

- Easy-to-use GUI
- two or three consecutive games on certain fields every week
- two teams can play each other 4 times maximum (may not be needed)
- adaptation for scheduling end-of-season tournaments 
  (make copy of schedule.generate() function, using point-based elimination algorithm for tournament scoring)
