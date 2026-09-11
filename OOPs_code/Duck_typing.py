class Duck:
    def sound(self):
        return 'Quack'

class Dog:
    def sound(self):
        return 'Brack'
def make_sound(animal):
    print(animal.sound())

make_sound(Dog())
make_sound(Duck())
    
        