class Device:
    def __init__(self, name, connectedBy):
        self.Name = name
        self.ConnectedBy = connectedBy
        self.Connected = True

    def __str__(self):
        return f"{self.Name} device is connected By {self.ConnectedBy}."

    def Disconnected(self):
        self.Connected = False
        print("Disconnected Successfully.")


mobile = Device("Mobile", "Charger")
print(mobile)
print(mobile.Disconnected())

class Mobile(Device):
    def __init__(self,name,connectedBy):
        self.ConnectedBy = connectedBy

