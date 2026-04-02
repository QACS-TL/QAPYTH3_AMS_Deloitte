class Animal:
    name = "Anon"
    colour = "Black"
    _limb_count = 4

    def get_limb_count(self):
        return self._limb_count

    def set_limb_count(self, value):
        if value < 0:
            value = 0
        self._limb_count = value

    limb_count = property(get_limb_count, set_limb_count)

    def eat(self, food):
        return f"I'm an {self.colour} animal called {self.name} using some of my {self._limb_count} limbs to eat {food} "

    def move(self, direction="up", distance="10"):
        return f"I'm an {self.colour} animal called {self.name} using some of my {self._limb_count} limbs to move {direction} for {distance} metres"
