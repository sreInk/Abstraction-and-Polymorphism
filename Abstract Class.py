from abc import ABC,abstractmethod
class abclass(ABC):
    def print(self,x):
        print("Passed Value ", x)
    @abstractmethod
    def task(self):
        print("We are Abstart")
class ts(abclass):
    def task(self):
        print("We Are The Goat")
test_obj = ts()
test_obj.task()
test_obj.print(100)