from television import tvShow, anime, isekai, scifi, drama, scifiAnime

def main():
    print(("*"*8)+"Subclass of a Subclass"+("*"*8))
    konosuba = isekai(title="KonoSuba: God's Blessing on this Wonderful World!",episodeCount=22,year=2016,animationStudio="Studio Deen", arrivalMethod="Died of Shock") # isekai subsubclass test
    print(konosuba.info())
    print(("*"*8)+"Subclass of a Subclass part 2"+("*"*8))
    rebels = scifi(title="Star Wars: Rebels", episodeCount=75, year=2014, franchise="Star Wars")
    print(rebels.info())
    print(("*"*8)+"@Property decorator test"+("*"*8))
    breakingbad = drama(title="Breaking Bad", episodeCount=62, year=2008, episodeLengthAvg=45)
    print(breakingbad.info())
    print("The full viewing time of "+breakingbad.title+" is "+ breakingbad.fullViewingTime+".")
    print(("*"*8)+"Multi Inheritance using super()"+("*"*8))
    visions = scifiAnime(title="Star Wars: Visions", episodeCount=9, year=2021, franchise="Star Wars", animationStudio="Qubic Pictures")
    print(visions.info())

main()