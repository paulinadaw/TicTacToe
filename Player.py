class Player:

    def __init__(self, name):
        self.name = name

    def is_valid(self):
        if type(self.name) is not str or len(self.name) == 0:
            return False
        return True
