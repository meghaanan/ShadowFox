# Base class for general devices
class BasicDevice:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"{self.brand} {self.model} initialized as a Basic Device.")

    def device_info(self):
        return f"Device: {self.brand} {self.model}"


# Derived class for mobile phones
class MobilePhone(BasicDevice):
    def __init__(self, brand, model, phone_number):
        # Calling the parent class constructor using super()
        super().__init__(brand, model)
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []
        print(f"Mobile Phone with number {self.phone_number} initialized.")

    def make_call(self, number):
        print(f"Calling {number} from {self.phone_number}...")
        self.call_history.append(f"Outgoing call to {number}")

    def receive_call(self, number):
        print(f"Incoming call from {number}...")
        self.call_history.append(f"Incoming call from {number}")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")
        self.messages.append({"to": number, "message": message})

    def receive_message(self, number, message):
        print(f"Message received from {number}: {message}")
        self.messages.append({"from": number, "message": message})

    def take_a_picture(self):
        print("Taking a picture...")
        return "Picture taken"

    def show_call_history(self):
        print("\nCall History:")
        for call in self.call_history:
            print(f"- {call}")

    def show_messages(self):
        print("\nMessages:")
        for msg in self.messages:
            if "to" in msg:
                print(f"Sent to {msg['to']}: {msg['message']}")
            elif "from" in msg:
                print(f"Received from {msg['from']}: {msg['message']}")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.phone_number})"


# Example usage
if __name__ == "__main__":
    # Creating an instance of MobilePhone
    my_phone = MobilePhone("Apple", "iPhone 15", "+1234567890")
    
    # Displaying device info
    print(my_phone.device_info())
    
    # Testing functionalities
    my_phone.make_call("+0987654321")
    my_phone.receive_call("+1122334455")
    my_phone.send_message("+0987654321", "Hello! How are you?")
    my_phone.receive_message("+1122334455", "Hey! I'm doing great.")
    my_phone.take_a_picture()
    
    # Displaying call history and messages
    my_phone.show_call_history()
    my_phone.show_messages()
