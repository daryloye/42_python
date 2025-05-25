from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King Class"""

    def set_eyes(self, eyes):
        """Set eye colour"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set hair colour"""
        self.hairs = hairs

    def get_eyes(self):
        """Get eye colour"""
        return (self.eyes)

    def get_hairs(self):
        """Get hair colour"""
        return (self.hairs)
