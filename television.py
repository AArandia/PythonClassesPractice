import datetime

class tvShow:
    def __init__(self, title, episodeCount, year,**kwargs):
        self.title = title
        self.episodeCount = episodeCount
        self.year = year
        assert not kwargs
    def info(self):
        return "Title: "+self.title+"\nEpisode Count: "+str(self.episodeCount)+\
            "\nYear: "+str(self.year)


class anime(tvShow):
    def __init__(self, animationStudio, **kwargs):
        self.animationStudio = animationStudio
        super().__init__(**kwargs)
    
    def info(self):
        return super().info()+"\nAnimation Studio: "+self.animationStudio


class scifi(tvShow):
    def __init__(self, franchise, **kwargs):
        self.franchise = franchise
        super().__init__(**kwargs)

    def info(self):
        return super().info()+"\nFranchise: "+self.franchise


class isekai(anime):
    def __init__(self, arrivalMethod, **kwargs):
        self.arrivalMethod = arrivalMethod
        super().__init__(**kwargs)
    
    def info(self):
        return super().info()+"\nIsekai Arrival Method: "+self.arrivalMethod


class scifiAnime(scifi,anime):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def info(self):
        return super().info()


class drama(tvShow):
    def __init__(self, episodeLengthAvg, **kwargs):
        self.episodeLengthAvg = episodeLengthAvg
        super().__init__(**kwargs)
    
    @property
    def fullViewingTime(self):
        return str(datetime.timedelta(minutes = (self.episodeLengthAvg * self.episodeCount)))
    
    def info(self):
        return super().info()