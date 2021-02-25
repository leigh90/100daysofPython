# CLASS INHERITANCE
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

# to inherit from a class you pass the name of the class in the brackets when you create the class
class Fish(Animal):
    def __init__(self):
        # super() refers to the superclass in this case the Animal Class that Fish is inheriting from.
        # What this line says is essentially initialize this object with everything the super class has/inherit what super class has.
        super(). __init__()

    def swim(self):
        print("Moving in water")
    # say you want to extend a superclass method e.g you want the same functionality as the superclass
    # but also want to add a  little bit extra.
    def breathe(self):
        # this allows you to inherit the functionality from the super class' breathe method and then extend it.
        super().breathe()
        print("doing this underwater")


nemo = Fish()
nemo.swim()
# the breathe method and num_eyes attribute though not explicitly mentioned in the fish class have been inherited from the Animal class
nemo.breathe()
print(nemo.num_eyes)