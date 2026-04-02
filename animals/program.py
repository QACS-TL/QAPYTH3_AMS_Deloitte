from animal import Animal

ani1 = Animal(name="Fifi", colour="blue", limb_count=6)
ani2 = Animal()

# ani1.name = "Fifi"
# ani1.colour = "blue"
# ani1.limb_count = -1
# ani1.color = 560

ani2.name = "Fido"
ani2.colour = "red"
ani2.limb_count = 5
print(ani2.limb_count)

print(ani1.eat("fish"))
print(ani2.eat("bananas"))

print(ani1)
