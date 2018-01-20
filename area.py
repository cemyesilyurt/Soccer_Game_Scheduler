"""
File area.
Defines class Area.
"""
"""
Original Contributor: Cem Hasan Mehmet Yesilyurt
Last Modified: December 20, 2017
"""

import region

class Area:
    """
    One object of this class represents one area.
    """
    
    def __init__(self, name):
        """
        Sets area's name and regions.
        """
        self.name = name
        self.regions = []
        
    def addRegion(self, region):
        """
        Adds one region to object's list of regions.
        """
        self.regions.append(region)
        
    def __str__(self):
        """
        Returns string of object.
        """
        return 'Area ' + self.name