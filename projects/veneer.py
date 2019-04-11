class Art:
    def __init__(self, artist, title, medium, year):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.representative_string = """{artist}. "{title}". {year}, {medium}""".format(artist=self.artist, title=self.title, year=self.year, medium=self.medium)

    def __repr__(self):
        return self.representative_string

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910)

print(girl_with_mandolin)