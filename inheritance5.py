class SamsungPhone:
    def __init__(self, model, color, storage, battery, release_year, price):
        self.model = model
        self.color = color
        self.storage = storage  # in GB
        self.battery = battery  # in mAh
        self.release_year = release_year
        self.price = price  # in USD

    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Storage: {self.storage}GB")
        print(f"Battery: {self.battery}mAh")
        print(f"Release Year: {self.release_year}")
        print(f"Price: ${self.price}")
        print("-" * 40)

samsung1 = SamsungPhone(model="Galaxy S21", color="Phantom Gray", storage=128, battery=4000, release_year=2021, price=799)
samsung2 = SamsungPhone(model="Galaxy S21 Ultra", color="Phantom Black", storage=256, battery=5000, release_year=2021, price=1199)
samsung3 = SamsungPhone(model="Galaxy Z Fold 4", color="Burgundy", storage=512, battery=4400, release_year=2022, price=1799)
samsung4 = SamsungPhone(model="Galaxy A53", color="Awesome Blue", storage=128, battery=5000, release_year=2022, price=449)
samsung5 = SamsungPhone(model="Galaxy S23 Ultra", color="Green", storage=1024, battery=5000, release_year=2023, price=1399)


samsung1.display_info()
samsung2.display_info()
samsung3.display_info()
samsung4.display_info()
samsung5.display_info()
