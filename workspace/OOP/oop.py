class Animal():
    habitat='land'
    def __init__(self,a,b,c=1):
        self.limbs=b
        self.tail=c
        self.animaltype=a
        
    def animaldetails(self,color,hair,breed):
        print('Color of the '+self.animaltype+' is '+color)
        print('Hair type is  '+hair)
        print('Breed of the '+self.animaltype+' is '+breed)
        
dog=Animal('dog',4,1)
print(dog.limbs)
print(dog.tail)
print(dog.habitat)
print(dog.animaltype)
dog.animaldetails('Brown','Long','Labradir')