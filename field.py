"""
File field.
Defines class Field.
"""
"""
Original Contributor: Cem Hasan Mehmet Yesilyurt
Last Modified: December 20, 2017
"""

import region
import division
import timeSlot
from functools import total_ordering

@total_ordering
class Field:
    """
    One object of this class represents one playing field.
    """
    
    def __init__(self, name, region, divisions, timeSlots):
        """
        Sets object's name, region, divisions, timeSlots, home teams, and number of games.
        """
        self.name = name
        self.region = region
        self.divisions = divisions
        self.timeSlots = timeSlots
        self.homeTeams = []
        self.numGames = 0      
        
    def addHomeTeam(self, homeTeam):
        """
        Adds a home team to this object.
        """
        self.homeTeams.append(homeTeam)
            
    def incNumGames(self):
        """
        Increments the number of games of the object.
        """        
        self.numGames += 1
    
    def __eq__(self, other):
        """
        Returns true if self and other have same name.
        """
        return self.name == other.name
    
    def __lt__(self, other):
        """
        Returns true if self's name is less than other's name.
        """
        return self.name < other.name
        
    def __str__(self):
        """
        Returns string of object.
        """
        return self.name