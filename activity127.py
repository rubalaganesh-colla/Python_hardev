from abc import ABC, abstractmethod
class ABsclass(ABC):
   def print(self,x):
       print("Base value",x)
   @abstractmethod
   def task(self):
      print("we are in the ABsclass task")
class test_class(ABsclass):
   def task(self):
       print("we are in the test_class task")
obj=test_class()
obj.print(10)
obj.task()
