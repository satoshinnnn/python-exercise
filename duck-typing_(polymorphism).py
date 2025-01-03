# Animal Sound Simulator
class Dog:
    def make_sound(self):   
        print("woof woof")
class Cat:
    def make_sound(self):
        print("Meow Meow")
class Cow:
    def make_sound(self):
        print("Moo Moo")

# hàm trigger phương thức make_sound() 
def play_a_sound(animals):
    for animal in animals:
        animal.make_sound()   # Duck-typing adoption: các con Dog, Cat, Cow có chung method 'make_sound'  

# lập list đối tượng các conn vật
animals = [ Dog(), Cat(), Cow()]

# gọi hàm
play_a_sound(animals)
