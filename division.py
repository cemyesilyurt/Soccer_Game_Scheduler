"""
File divisions.
Defines class Division.
"""
"""
Original Contributor: Cem Hasan Mehmet Yesilyurt
Last Modified: December 20, 2017
"""

import team

class Division:
    """
    One object of this class represents one division.
    """
    
    def __init__(self, name):
        """
        Sets name of object and its teams.
        """
        self.name = name
        self.teams = []
    
    def addTeam(self, team):
        """
        Adds team to the object's teams list.
        """
        self.teams.append(team)
        
    def __str__(self):
        """
        Returns string of object.
        """
        return self.name
        
if __name__ == "__main__":
    d = Division('U12')
    