class PhoneBattery:
    def __init__(self, percent):
        self.percent = percent

    def use(self, amount):
        self.percent -= amount
        if self.percent <= 0:
            self.percent = 0
            print("Quvvat tugadi")
        else:
            print(f"Batareya: {self.percent}%")

    def charge(self, amount):
        self.percent += amount
        if self.percent > 100:
            self.percent = 100
        print(f"Batareya: {self.percent}%")


# Obyekt
phone = PhoneBattery(50)
phone.use(20)
phone.use(40)
phone.charge(30)
