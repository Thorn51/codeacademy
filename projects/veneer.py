class Art:
    def __init__(self, artist, title, medium, year):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.representative_string = """{artist}. "{title}". {year}, {medium}""".format(artist=self.artist, title=self.title, year=self.year, medium=self.medium)

    def __repr__(self):
        return self.representative_string

class MarketPlace:
    def __init__(self):
        self.listings = []

    def add_listings(self, new_listings):
        self.listings.append(new_listings)

    def remove_listings(self, sold):
        self.listings.remove(sold)

    def show_listings(self):
        for listing in self.listings:
            print(self.listings)


veneer = MarketPlace()

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910)

print(veneer.show_listings())