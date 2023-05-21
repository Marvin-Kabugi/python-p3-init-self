#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt") -> None:
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def showing_self(self):
        return self
    
    def adopt(self, owner_name):
        self.owner = owner_name


# fido = Dog("Fido")
# fido.name

# snoopy = Dog("Snoopy")
# snoopy.name