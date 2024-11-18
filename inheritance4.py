class ApplePhone:
    def __init__(self, model, color, storage, release_year, price):
        self.model = model
        self.color = color
        self.storage = storage  # in GB
        self.release_year = release_year
        self.price = price  # in USD

    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Storage: {self.storage}GB")
        print(f"Release Year: {self.release_year}")
        print(f"Price: ${self.price}")
        print("-" * 40)

iphone1 = ApplePhone(model="iPhone 12", color="Black", storage=128, release_year=2020, price=799)
iphone2 = ApplePhone(model="iPhone 13 Pro", color="Silver", storage=256, release_year=2021, price=999)
iphone3 = ApplePhone(model="iPhone 14", color="Blue", storage=512, release_year=2022, price=1099)
iphone4 = ApplePhone(model="iPhone SE (3rd Gen)", color="Red", storage=64, release_year=2022, price=429)
iphone5 = ApplePhone(model="iPhone 15 Pro Max", color="Titanium", storage=1_024, release_year=2023, price=1599)


iphone1.display_info()
iphone2.display_info()
iphone3.display_info()
iphone4.display_info()
iphone5.display_info()
