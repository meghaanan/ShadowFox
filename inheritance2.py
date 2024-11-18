class MobilePhone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

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
    my_phone = MobilePhone("Samsung", "Galaxy S23", "+1234567890")
    
    # Testing functionalities
    print(my_phone)

    # Making and receiving calls
    my_phone.make_call("+0987654321")
    my_phone.receive_call("+1122334455")

    # Sending and receiving messages
    my_phone.send_message("+0987654321", "Hello, how are you?")
    my_phone.receive_message("+1122334455", "Hi! I'm good, thanks!")

    # Taking a picture
    my_phone.take_a_picture()

    # Displaying call history and messages
    my_phone.show_call_history()
    my_phone.show_messages()
