zoo = ("Bear", "Wolf", "Eagle", "Python", "Unicorn", "Squirrel", "Rabbit", "Dog", "Tiger", "Lion")

zoo.index("Python")

animal_to_find = "Kangaroo"
animal_to_find = "Dog"

if animal_to_find in zoo:
    print("Found Animal")

else: print("Not found")

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eigth_animal, ninth_animal, tenth_animal) = zoo

print(first_animal)
print(second_animal)
print(third_animal)
print(fourth_animal)
print(fifth_animal)

zoo_list = []

for animal in zoo:
    zoo_list.append(animal)

more_animals = ["mouse", "Griffin", "bird"]

zoo_list.extend(more_animals)


print(zoo_list)