#ACTIVITY 1: INHERITANCE
# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Child class 
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  
        self.storage = storage
        self.battery = battery

    def call(self, contact):
        print(f"calling {contact} using {self.device_info()}..")

    def charge(self):
        print(f"Charging {self.device_info()}... Battery: {self.battery}%")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.device_info()}")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S23", "256GB", 85)
phone1.call("Alice")
phone1.charge()
phone1.install_app("WhatsApp")
