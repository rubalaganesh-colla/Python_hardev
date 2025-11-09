class MYclass:
    _privateVar = 27
    def _privMeth(self):
           print("This is a private method")
    def hello(self):
           print("private var is:", self._privateVar)
foo = MYclass()
foo.hello()
foo._privMeth 