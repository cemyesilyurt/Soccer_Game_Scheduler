"""
File game.
Defines class Game.
"""
"""
Original Contributor: Cem Hasan Mehmet Yesilyurt
Last Modified: December 20, 2017
"""

class Game:
    """
    One object of this class represents one game.
    """
    
    def __init__(self, homeTeam, awayTeam, division, field, timeSlot):
        """
        Sets object's home team, away team, division, field, and timeSlot.
        """
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.division = division
        self.field = field
        self.region = self.field.region
        self.timeSlot = timeSlot
        
    def __str__(self):
        """
        Returns string of object.
        """
        if self.homeTeam.name == 'Bye' or self.awayTeam.name == 'Bye':
            return str(self.timeSlot.start) + ', ' + 'Bye'
        else:
            return str(self.timeSlot.start) + ', ' + str(self.homeTeam) + ', ' + str(self.awayTeam) + ', ' + str(self.field) + ', ' + str(self.division) + ', ' + str(self.region)    
    
    def __lt__(self, other):
        """
        Returns true if self starts before other.
        """
        return self.timeSlot < other.timeSlot
        #return self.field < other.field