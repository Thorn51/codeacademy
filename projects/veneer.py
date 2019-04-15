class MarketPlace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listings(self, expired_listing):
        self.listings.remove(expired_listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)

class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return f"""{self.artist}. "{self.title}." {self.year}, {self.medium}. {self.owner.name}, {self.owner.location}."""

class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.is_museum = is_museum
        if is_museum:
            self.location = location
        else:
            self.location = "Private Collection"

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)

    def buy_artwork(self, artowork):
        if artowork.owner != self:
            art_listing = None
            for listing in veneer.listings:
                if listing.art == artowork:
                    art_listing = listing
                    break
            if art_listing != None:
                art_listing.art.owner = self
                veneer.remove_listings(art_listing)

class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        Client.name = seller

    def __repr__(self):
        return f"""{self.art.title} -- {self.price}"""


veneer = MarketPlace()

edytta = Client("Edytta Halpirt", None, False)

moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)

edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")

veneer.show_listings()

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)

veneer.show_listings()