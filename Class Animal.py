from abc import ABC,abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move (self):
        print("We are The Almight")

class Fish(Animal):
    def move (self):
        print("Gills Op in Chat")
      
class Aktuski(Animal):
    def move (self):
        print("We are The Gds")
      
class Porche(Animal):
    def move (self):
        print("We Need A writer")

R = Human()
R.move()
k = Fish()
k.move()
a = Aktuski()
a.move()
w = Porche()
w.move()
      
      