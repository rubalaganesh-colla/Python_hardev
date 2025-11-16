class flashcrad:
        def __init__(self, front, back):
                self.front = front
                self.back = back
        def _str_(self):
                return self.word+' ('+self.meaning+')'
flash = []
print ("welcome to flashcard app")
while (True):
        word = input("enter word:")
        meaning = input("enter meaning:")
        flash.append(flashcrad(word, meaning))
        choice = int(input("add 0 ,if you wantto add a new flashcard othewise enter 1:"))  
        if (choice == 1):                  
                    break
print("your flashcards are:",)
for card in flash:
        print(">",card)
