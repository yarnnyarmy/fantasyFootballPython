class Wr:

    def __init__(self):
        self.name = None
        self.team = None
        self.draftkings_points = None
        self.wr_id = None
        self.position = None
        self.salary = None

    def get_name(self):
        return self.name

    def get_team(self):
        return self.team

    def get_draftkings_points(self):
        return self.draftkings_points

    def get_id(self):
        return self.wr_id

    def get_position(self):
        return self.position

    def get_salary(self):
        return self.salary

        # setter method

    def set_name(self, name):
        self.name = name

    def set_team(self, team):
        self.team = team

    def set_draftkings_points(self, draftkings):
        self.draftkings_points = draftkings

    def set_id(self, wr_id):
        self.wr_id = wr_id

    def set_position(self, position):
        self.position = position

    def set_salary(self, salary):
        self.salary = salary