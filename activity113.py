class IOString():
    def __init__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = input("Enter a string: ")
    def print_string(self):
        print(self.str1.upper())
        print(self.str1.lower())
        print(self.str1.title())
        print(self.str1.capitalize())
        print(self.str1.count("a"))
        print(self.str1.replace("a", "@"))
        print(self.str1.index("siva"))
str1 = IOString()
str1.get_string()
str1.print_string()
