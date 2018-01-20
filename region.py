"""
File region.
Defines class Region.
"""
"""
Original Contributor: Cem Hasan Mehmet Yesilyurt
Last Modified: December 20, 2017
"""

import division
import field

class Region:
    """
    One object of this class represents one region.
    """
    
    def __init__(self, name):
        """
        Sets object's name, divisions, fields, and teams.
        """
        self.name = name
        self.divisions = []
        self.fields = []
        self.teams = []
        
    def addDivision(self, division):
        """
        Adds a division to object's list of divisions.
        """
        self.division.append(division)
        
    def addField(self, field):
        """
        Adds a field to object's list of fields.
        """
        self.fields.append(field)        
    
    def addTeam(self, team):
        """
        Adds a team to object's list of teams.
        """
        self.teams.append(team)        
    
    
    def __str__(self):
        """
        Returns string of object.
        """
        return self.name
        