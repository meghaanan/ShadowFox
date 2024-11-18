
class MobilePhone:
    def __init__(self, model, screen_type="Touch Screen", network_type="5G", dual_sim=True, 
                 front_camera="12MP", rear_camera="48MP", ram="4GB", storage="64GB"):
        self.model = model
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def phone_info(self):
        print(f"Model: {self.model}")
        print(f"Screen Type: {self.screen_type}")
        print(f"Network Type: {self.network_type}")
        print(f"Dual SIM: {'Yes' if self.dual_sim else 'No'}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")

    def make_call(self, number):
        print(f"{self.model} is calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")



class Apple(MobilePhone):
    def __init__(self, model, ios_version, screen_type="Touch Screen", network_type="5G", dual_sim=False, 
                 front_camera="12MP", rear_camera="48MP", ram="4GB", storage="64GB"):
        super().__init__(model, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.ios_version = ios_version

    def use_face_id(self):
        print(f"{self.model} is using Face ID for unlocking.")

    def phone_info(self):
        super().phone_info()
        print(f"iOS Version: {self.ios_version}")



class Samsung(MobilePhone):
    def __init__(self, model, android_version, screen_type="Touch Screen", network_type="5G", dual_sim=True, 
                 front_camera="16MP", rear_camera="48MP", ram="4GB", storage="64GB"):
        super().__init__(model, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.android_version = android_version

    def use_fingerprint(self):
        print(f"{self.model} is using Fingerprint Scanner for unlocking.")

    def phone_info(self):
        super().phone_info()
        print(f"Android Version: {self.android_version}")



if __name__ == "__main__":
    print("Apple Phone Details:")
    iphone = Apple(model="iPhone 15", ios_version="iOS 17", front_camera="12MP", rear_camera="48MP", ram="4GB", storage="128GB")
    iphone.phone_info()
    iphone.make_call("+1234567890")
    iphone.use_face_id()

    print("\n" + "-"*40 + "\n")

    print("Samsung Phone Details:")
    galaxy = Samsung(model="Galaxy S23", android_version="Android 14", dual_sim=True, front_camera="16MP", rear_camera="108MP", ram="8GB", storage="256GB")
    galaxy.phone_info()
    galaxy.make_call("+0987654321")
    galaxy.use_fingerprint()
