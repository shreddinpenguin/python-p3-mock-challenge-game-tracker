class Game:
    all = []
    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) is str and not hasattr(self, "title") and len(title) > 0:
            self._title = title

    def results(self):
        return [game for game in Result.all if game.game is self]

    def players(self):
        return list({game.player for game in self.results()})

    def average_score(self, player):
        return sum(player.score for player in self.results()) / len(self.results())

class Player:
    all = []
    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if type(username) is str and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return [player for player in Result.all if player.player is self]

    def games_played(self):
        return list({player.game for player in self.results()})

    def played_game(self, game):
       return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if type(score) is int and 1 <= score <= 5000 and not hasattr(self, "score"):
            self._score = score

    # @property
    # def player(self):
    #     return self._player
    
    # @player.setter
    # def player(self, player):
    #     if type(player) is Player:
    #         self._player = player

    # @property
    # def game(self):
    #     return self._game
    
    # @game.setter
    # def player(self, game):
    #     if type(game) is Game:
    #         self._game = game