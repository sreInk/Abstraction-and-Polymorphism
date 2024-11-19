class india():
    def captital(self):
        print("New Delhi")
    def Aliance(self):
        print("USA")
    def Language(self):
        print("Hindi")
class US():
    def captital(self):
        print("Washington D.C")
    def Aliance(self):
        print("India")
    def Language(self):
        print("Englis")
obj_india = india()
obj_us = US()
for country in (obj_india,obj_us):
    country.captital()
    country.Aliance()
    country.Language()
