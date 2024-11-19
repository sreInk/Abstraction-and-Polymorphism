class Ferrari():
    def Millage(self):
        print("More than ever")
    def Fuel(self):
        print("1L")
    def Speed(self):
        print("340")
class Bmw():
    def Millage(self):
        print("200watt")
    def Fuel(self):
        print("2L")
    def Speed(self):
        print("290")
obj_india = Bmw()
obj_us = Ferrari()
for country in (obj_india,obj_us):
    country.Millage()
    country.Speed()
    country.Fuel()
