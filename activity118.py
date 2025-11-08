class bird:
    def _int_(self):
        print("bird is ready")
    def whoisThis(self):
        print("bird")
    def swim(self):
        print("swim faster")
class penguin(bird):
    def _int_(self):
        bird._int_(self)
        print("penguin is ready")
    def whoisThis(self):
        print("penguin")
    def run(self):
        print("run faster")
peggy = penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()