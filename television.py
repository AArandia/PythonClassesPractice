import datetime

class tvShow:
    def __init__(self, title, episodeCount, year):
        self.title = title
        self.episodeCount = episodeCount
        self.year = year
    def info(self):
        return "Title: "+self.title+"\nEpisode Count: "+str(self.episodeCount)+\
            "\nYear: "+str(self.year)


class anime(tvShow):
    def __init__(self, title, episodeCount, year, animationStudio):
        self.animationStudio = animationStudio
        super().__init__(title, episodeCount, year)
    
    def info(self):
        return super().info()+"\nAnimation Studio: "+self.animationStudio


class scifi(tvShow):
    def __init__(self, title, episodeCount, year, franchise):
        self.franchise = franchise
        super().__init__(title, episodeCount, year)

    def info(self):
        return super().info()+"\nFranchise: "+self.franchise


class isekai(anime):
    def __init__(self, title, episodeCount, year, animationStudio, arrivalMethod):
        self.arrivalMethod = arrivalMethod
        super().__init__(title, episodeCount, year, animationStudio)
    
    def info(self):
        return super().info()+"\nIsekai Arrival Method: "+self.arrivalMethod


class drama(tvShow):
    def __init__(self, title, episodeCount, year, episodeLengthAvg):
        self.episodeLengthAvg = episodeLengthAvg
        super().__init__(title, episodeCount, year)
    
    @property
    def fullViewingTime(self):
        return str(datetime.timedelta(minutes = (self.episodeLengthAvg * self.episodeCount)))



