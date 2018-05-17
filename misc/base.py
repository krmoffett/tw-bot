class Player():
    def __init__(self, name=None, chars="", ships=""):
        self.name = name
        self.assigned_chars = chars
        self.assigned_ships = ships
    def get_name(self):
        return self.name

    def get_chars(self):
        return self.assigned_chars

    def get_ships(self):
        return self.assigned_ships