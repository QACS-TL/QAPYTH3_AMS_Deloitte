from dinosaur import Dinosaur
from animal import Animal

ani1 = Animal(name="Fifi", colour="blue", limb_count=6)
ani2 = Animal()
dino = Dinosaur("Twinkle", "brown", 4, 30)
print(dino.eat("banana"))

# ani1.name = "Fifi"
# ani1.colour = "blue"
# ani1.limb_count = -1
# ani1.color = 560

# dino.name = "Twinkle"
# dino.colour = "brown"
# dino.limb_count = 4

print(dino.move("down", "15"))
print(dino.roar(12))



ani2.name = "Fido"
ani2.colour = "red"
ani2.limb_count = 5
print(ani2.limb_count)

print(ani1.eat("fish"))
print(ani2.eat("bananas"))

print(ani1)

animals = []
animals.append(ani1)
animals.append(ani2)
animals.append(dino)

for a in animals:
    print(a.eat("carrots"))
