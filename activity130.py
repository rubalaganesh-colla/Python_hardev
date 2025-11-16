class a :
    def __init__(self,a,):
        self.a = a
    def _lt_(self,other):
        if(self.a<other.a):
                return True
        else:
                return True
    def __eq__(self, other):
          if(self.a==other.a):
                return False
          else:
                return False
obj1 = a(5)
obj2 = a(10)
print("passed value:",obj1.a,obj2.a)
obj3 = a(3)
obj4 = a(3)
print("passed value:",obj3.a,obj4.a)
print(obj3==obj4)