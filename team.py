"""
File team.
Defines class Team.
"""
"""
Original Contributor: Cem Hasan Mehmet Yesilyurt
Last Modified: December 20, 2017
"""

import region
import division
import game
from functools import total_ordering

@total_ordering
class Team:
    """
    One object of this class represents one team.
    """
    
    def __init__(self, name, gender, region, division, homeField, numWeeks):
        """
        Sets name, gender, region, division, homeField, games, number of home games, and number of away games, 
        weekly availability of object, and home-away record.
        """        
        self.name = name
        self.gender = gender
        self.region = region
        self.division = division        
        self.homeField = homeField
        self.games = []
        self.numHomeGames = 0
        self.numAwayGames = 0
        self.weekly_availability = []
        for i in range(0,numWeeks):
            self.weekly_availability.append(True)
        self.homeAwayRecords = []
        for i in range(0,numWeeks):
            self.homeAwayRecords.append('')  # entries will be filled with 'home' or 'away', for the corresponding week
    
    def addGame(self, game):    
        """
        Adds game to object's games list.  Updates number of home games and away games.
        """
        self.games.append(game)
        if game.homeTeam is self:
            self.numHomeGames += 1
        else:
            self.numAwayGames += 1    
    
    def isAvailable(self, week_index):
        """
        Returns availability of team for given week.
        """
        return self.weekly_availability[week_index]
    
    def book(self, week_index):
        """
        Sets availability to false for given week.
        """
        self.weekly_availability[week_index] = False        
        
    def __str__(self):
        """
        Returns string of object.
        """
        return self.name + ' ' + self.gender
    
    def __eq__(self, other):
        """
        Returns true if self and other have the same name and gender.
        """
        return self.name == other.name and self.gender == other.gender
    
    def __lt__(self, other):
        """
        Returns true if self is alphabetically less than other.
        """
        return self.name < other.name