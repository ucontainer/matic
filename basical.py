
class User():
    def __init__(self,name, city, state):
        self.city = city
        self.state = state
        self.name = name
    def desc(self):
        self_desc = print(self.name+" from "+self.city+", "+self.state)
        return self_desc
user1 = User("Winston","Cleveland","Ohio")
user1.desc() 

class Puppy(User):
    def __init__(self, name, city, state):
        super().__init__(name, city, state)
puppy1 = Puppy("duggo","Houston","TX")
print(puppy1.desc())
    

game_genre = "action-adventure"
game = "The Last Stand"
print("F strings: ")
print(f"My fav game in {game_genre} genre is \"{game}\".")


original_text = "Jython"
fixed_text="P"+original_text[1:]
print("\nFixing strings by slicing")
print(f"Original text: {original_text}")
print(f"Fixed text: {fixed_text}")

text = "hello world"
print(text.capitalize())
print(text.title())
    
        
    
        
         
    




    
    
    




    


        