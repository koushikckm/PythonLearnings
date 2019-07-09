from abc import ABC,abstractmethod

class Restaurant(ABC):
    @abstractmethod
    def dininghall(self):
        pass
    
class FiveStar(Restaurant):
    def swimmingpool(self):
        print("Yes there is a swimming pool")
        
class BeachSideResort(Restaurant):
    def beachsidecafe(self):
        print("Yes there is a beachside cafe")
        
        
fs=FiveStar()
fs.swimmingpool()

bc=BeachSideResort()
bc.beachsidecafe()