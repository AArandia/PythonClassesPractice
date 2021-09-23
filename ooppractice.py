from television import tvShow, anime, isekai, scifi

def main():
    konosuba = isekai("KonoSuba: God's Blessing on this Wonderful World!",22,2016,"Studio Deen", "Died of Shock") # isekai subsubclass test
    # konosuba = anime("KonoSuba: God's Blessing on this Wonderful World!",22,2016,"Studio Deen") # anime subclass test
    # konosuba = tvShow("KonoSuba: God's Blessing on this Wonderful World!",22,2016) # tvShow class test
    print(konosuba.info())
    print("*"*32)
    rebels = scifi("Star Wars: Rebels",75,2014,"Star Wars")
    print(rebels.info())

main()