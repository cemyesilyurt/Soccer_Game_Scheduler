"""
File schedule.
Defines class Schedule.
"""
"""
Original Contributor: Cem Hasan Mehmet Yesilyurt
Last Modified: December 20, 2017
"""

import random
from game import Game

class Schedule:
    """
    One object of this class is one schedule.
    """
    
    def __init__(self, teams, division, gender, NUM_WEEKS, PREFERRED_HOURS):
        """
        Sets the teams, division, gender, number of weeks, and preferred hours of object.
        """
        self.games = []
        self.teams = teams
        self.division = division
        self.gender = gender
        self.NUM_WEEKS = NUM_WEEKS
        self.PREFERRED_HOURS = PREFERRED_HOURS
            
    
    def generate(self):
        """
        Modifies attribute variables to reflect new schedule.
        """

        # scheduling objectives:
        # ten games maximum
        # about five home games per team
        # about five away games per team
        # preferred order: home, away, home, ...
        #              or: away, home, away, ...
        # one game per week per team
        # games in preferred hours
            
        # working truncated round robin - with booking
        # NUM_ROUNDS = len(self.teams)-1  # for full round robin, use this for while loop condition
        MID_INDEX = int(len(self.teams)/2)
        this_week = 0        
        
        # for each round
        while this_week < self.NUM_WEEKS:
            
            #For debugging:
            #print('week ' + str(this_week) + ':')
            
            # partition teams
            top_row = self.teams[0:MID_INDEX]
            bot_row = self.teams[MID_INDEX:]
            bot_row.reverse()
            
            # assign games
            for j in range(0, MID_INDEX):
                thisTeam = top_row[j]
                otherTeam = bot_row[j]
                
                if this_week == 0:
                    # make thisTeam the home team
                    self.bookGame(thisTeam, otherTeam, self.division, this_week, self.PREFERRED_HOURS, self.games)
                    
                else:
                    
                    # do not want three home games or three away games in a row.  Two in a row is acceptable.
                    # want about five home games and five away games.  This holds for 8 teams or more.  Get 3-7 when 6 teams or less.
                    last_week = this_week - 1
                    week_before = this_week - 2
                    
                    if this_week == 1:
                                        
                        if thisTeam.homeAwayRecords[last_week] == 'home' and otherTeam.homeAwayRecords[last_week] == 'away':
                            # make thisTeam the away team and otherTeam the home team
                            self.bookGame(otherTeam, thisTeam, self.division, this_week, self.PREFERRED_HOURS, self.games)
                                        
                        elif thisTeam.homeAwayRecords[last_week] == 'away' and otherTeam.homeAwayRecords[last_week] == 'home':
                            # make thisTeam the home team and otherTeam the away team
                            self.bookGame(thisTeam, otherTeam, self.division, this_week, self.PREFERRED_HOURS, self.games)
                        
                        elif thisTeam.homeAwayRecords[last_week] == 'home' and otherTeam.homeAwayRecords[last_week] == 'home':
                            # make thisTeam the home team
                            self.bookGame(thisTeam, otherTeam, self.division, this_week, self.PREFERRED_HOURS, self.games)
                        
                        elif thisTeam.homeAwayRecords[last_week] == 'away' and otherTeam.homeAwayRecords[last_week] == 'away':
                            # make thisTeam the away team
                            self.bookGame(otherTeam, thisTeam, self.division, this_week, self.PREFERRED_HOURS, self.games)
            
                    elif this_week >= 2:                                        
                        
                        if thisTeam.homeAwayRecords[last_week] == 'home' and thisTeam.homeAwayRecords[week_before] == 'home':
                            # make thisTeam the away team
                            self.bookGame(otherTeam, thisTeam, self.division, this_week, self.PREFERRED_HOURS, self.games)
                            
                        elif thisTeam.homeAwayRecords[last_week] == 'away' and thisTeam.homeAwayRecords[week_before] == 'away':
                            # make thisTeam the home team
                            self.bookGame(thisTeam, otherTeam, self.division, this_week, self.PREFERRED_HOURS, self.games)
                        
                        elif thisTeam.homeAwayRecords[last_week] == 'home' and otherTeam.homeAwayRecords[last_week] == 'away':
                            # make thisTeam the away team and otherTeam the home team
                            self.bookGame(otherTeam, thisTeam, self.division, this_week, self.PREFERRED_HOURS, self.games)
                                        
                        elif thisTeam.homeAwayRecords[last_week] == 'away' and otherTeam.homeAwayRecords[last_week] == 'home':
                            # make thisTeam the home team and otherTeam the away team
                            self.bookGame(thisTeam, otherTeam, self.division, this_week, self.PREFERRED_HOURS, self.games)
                        
                        elif thisTeam.homeAwayRecords[last_week] == 'home' and otherTeam.homeAwayRecords[last_week] == 'home':
                            # make thisTeam the home team
                            self.bookGame(thisTeam, otherTeam, self.division, this_week, self.PREFERRED_HOURS, self.games)
                        
                        elif thisTeam.homeAwayRecords[last_week] == 'away' and otherTeam.homeAwayRecords[last_week] == 'away':
                            # make thisTeam the away team
                            self.bookGame(otherTeam, thisTeam, self.division, this_week, self.PREFERRED_HOURS, self.games)
            
            #For debugging:
            #for tm in self.teams:
            #    print(tm.homeAwayRecords)
                                    
            # update teams list
            self.teams.insert(1, self.teams.pop(len(self.teams)-1))
            this_week += 1

        # sort teams into alphabetical order
        self.teams.sort()


    def bookGame(self, homeTeam, awayTeam, division, this_week, PREFERRED_HOURS, games):    
        """
        Books a game for thisTeam as home team, otherTeam as away team, and adds game to lists.
        """
        # find an hour this week
        foundHour = False
        while not foundHour:
            # randomly choose hour index from preferred hours
            random.seed()
            this_hour = PREFERRED_HOURS[random.randint(0, len(PREFERRED_HOURS)-1)]                
            # Set time slot
            t = homeTeam.homeField.timeSlots[this_week][this_hour]
            # check availability of time slot -- if true, exit loop
            foundHour = t.isAvailable
        # Book time slot, home team, and away team
        t.book()        
        homeTeam.book(this_week)
        awayTeam.book(this_week)
        # Set home-away records for each team
        homeTeam.homeAwayRecords[this_week] = 'home'
        awayTeam.homeAwayRecords[this_week] = 'away'    
        # Set game
        g = Game(homeTeam, awayTeam, division, homeTeam.homeField, t)
        # Add game to game lists
        homeTeam.addGame(g)
        awayTeam.addGame(g)
        games.append(g)                           
        
    
    def getStrNumHomeAway(self):
        """
        Returns multi-line string of number of home and away games for each team.
        """
        s = 'NUMBER OF HOME AND AWAY GAMES BY TEAM:\n'
        for team in self.teams:
            if team.name == 'Bye':
                pass
            else:
                s += 'Team: %(name)20s   Home: %(num1)i  Away: %(num2)i  Total: %(total)i \n' % {'name': str(team), 'num1': team.numHomeGames, 'num2': team.numAwayGames, 'total': len(team.games)}
        return s
    
    #def getListNumHomeAway(self):
    
    
    def getStrTeamsSched(self, title):
        """
        Returns multi-line string of games for each team.
        """
        s = title + '\n\n'
        s += 'Date & Time, Home Team, Away Team, Field, Division, Region' + '\n'
        for team in self.teams:
            if team.name == 'Bye':
                pass
            else:
                s += team.name + ' ' + team.gender + "' Games:\n"
                team.games.sort()                        
                for g in team.games:
                    s += '    ' + str(g) + '\n'
            s += '\n'                
        return s
    
        
    def getStrTimesSched(self, title):
        """
        Returns multi-line string of games in chronological order.
        """
        s = title + '\n\n'    
        s += 'Date & Time, Home Team, Away Team, Field, Division, Region' + '\n'
        self.sortGamesByTime(self.games)
        
        game_index = 0
        week_index = 0
        NUM_GAMES_PER_WEEK = int(len(self.teams)/2)

        while week_index < self.NUM_WEEKS:
            s += 'Week ' + str(week_index+1) + ':\n'
            while game_index < NUM_GAMES_PER_WEEK * (week_index+1):
                s += '    ' + str(self.games[game_index]) + '\n'
                game_index += 1
            s += '\n'
            week_index += 1        

        return s
    

    def sortGamesByTime(self, bad_list):
        """
        Sorts a list by the time slots of its objects.
        """
        length = len(bad_list) - 1
        sorted = False
        while not sorted:
            sorted = True
            for i in range(length):
                if bad_list[i].timeSlot > bad_list[i+1].timeSlot:
                    sorted = False
                    bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]              
     