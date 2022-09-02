class FootballPlayers:
    Qb = []

    def __int__(self, name, pos, draftkings_points, draftkings_rank):
        self.name = name
        self.pos = pos
        self.draftkings_points = draftkings_points
        self.draftkings_rank = draftkings_rank
        self.Qb.append(self)

    def add(self, qbs):
        self.Qb.append(qbs)



