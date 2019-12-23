# I define my classes
class Animal:
    
    def __init__(self, name, weight):
        self.name = name
        print("My name is " + name)
        self.weight = weight
        print("My weight is " + str(weight) + " kg")
    
    def __gt__(self, other):
        return self.weight > other.weight
    
    def eats(self, food):
        print("Today " + self.name + " is fed " + str(food) + " kg of food")
        
        
class Cow(Animal):
    liter_produced = 10    
    
    def tells(self):
        print(self.name  + " says moo")
         
    def milk(self):
        print(self.name + " gives " + str(self.liter_produced) + " litres of milk")
        
    def eats(self, food):
        print(self.name + " is eating " + str(food) + " kg of grass")

        
class Goose(Animal): 
    def tells(self):
        print(self.name  + " says honk")
    def collect_eggs(self, eggs):
        print(self.name + " lays " + str(eggs) + " eggs per month")


class Sheep(Animal):            
    def tells(self):
        print(self.name  + " says baaah")
    def shear(self, times): 
        print(self.name  + " is sheared " + str(times) + " times per month")
        
class Hen(Goose):
    def tells(self):
        print(self.name  + " says cluck")
        
class Goat(Sheep, Cow):
    liter_produced = 2
    pass 

class Duck(Goose): 
    def tells(self):
        print(self.name  + " says quack")
        
#  I test my classes unitarily        
goose_Seryi = Goose("Seryi", 5)
goose_Seryi.eats(2)
goose_Seryi.tells()
goose_Seryi.collect_eggs(10)
goose_Belyi = Goose("Belyi", 4)
goose_Belyi.eats(3)
goose_Belyi.tells()
goose_Belyi.collect_eggs(8)
    
cow_Manka = Cow("Manka", 900)
cow_Manka.eats(10)
cow_Manka.milk()
cow_Manka.tells()

sheep_Barashek = Sheep("Barashek", 60)
sheep_Barashek.eats(6)
sheep_Barashek.tells()
sheep_Barashek.shear(2)
sheep_Kudriavyi = Sheep("Kudriavyi", 58 )
sheep_Kudriavyi.eats(5)  
sheep_Kudriavyi.tells()
sheep_Kudriavyi.shear(1)
    
hen_Kukareku = Hen("Kukareku", 3)
hen_Kukareku.eats(3)
hen_Kukareku.tells()
hen_Kukareku.collect_eggs(22)
hen_KoKo = Hen("KoKo", 4)
hen_KoKo.eats(4)
hen_KoKo.tells()
hen_KoKo.collect_eggs(27)

goat_Roga = Goat("Roga", 30)
goat_Roga.tells()
goat_Roga.eats(4)
goat_Roga.milk()

goat_Kopyta = Goat("Kopyta", 40)
goat_Kopyta.tells()
goat_Kopyta.eats(3)
goat_Kopyta.milk()

duck_Kriakva = Duck("Kriakva", 5)
duck_Kriakva.eats(3)
duck_Kriakva.tells()
duck_Kriakva.collect_eggs(18)

# I test a polymorphism with a loop
print("\n\n----------------------\n\n")

my_animals = [goose_Seryi, goose_Belyi, cow_Manka, sheep_Barashek, sheep_Kudriavyi, hen_Kukareku, hen_KoKo, goat_Roga, goat_Kopyta, duck_Kriakva]

heaviest_animal = hen_KoKo

for my_animal in my_animals:
    my_animal.tells()
    if isinstance(my_animal, Cow):
        my_animal.milk()
    if isinstance(my_animal, Goose):
        my_animal.collect_eggs(8)
    if isinstance(my_animal, Sheep) and not isinstance(my_animal, Goat):
        my_animal.shear(2)
    my_animal.eats(5)
    if my_animal > heaviest_animal:
        print(my_animal.name + " is heavier than " + heaviest_animal.name)
        heaviest_animal = my_animal
    else :
        print(my_animal.name + " is not heavier than " + heaviest_animal.name)
           
# I compute the total animal weight   
print("\n\n----------------------\n\n")

total_weight = 0
for my_animal in my_animals:
    total_weight = total_weight + my_animal.weight
print("The total weight is " + str(total_weight))
print("The heaviest animal is " + heaviest_animal.name) 




