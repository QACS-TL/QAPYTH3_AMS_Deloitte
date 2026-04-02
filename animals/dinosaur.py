from animal import Animal
class Dinosaur(Animal):
    def __init__(self, name, colour, limb_count=4, tooth_count=36):
        super().__init__(name, colour, limb_count)
        self.tooth_count = tooth_count

    @property
    def tooth_count(self):
        return self._tooth_count

    @tooth_count.setter
    def tooth_count(self, value):
        if value < 0:
            raise ValueError("Dinosaurs must have a positive number of teeth!")
        self._tooth_count = value

    def eat(self, food):
        #return f"I'm a DINOSAUR!!! called {self.name} ripping {food} to shreds with my {self.tooth_count} sharp teeth."
        return f"{super().eat(food)}. Actually I'm a dinosaur."

    def roar(self, volume):
        return f"I'm a dinosaur called {self.name} roaring with volume {volume}!"