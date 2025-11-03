class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()
