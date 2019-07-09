class Soldier:
    def __init__(self,candidateage):
        self.joinage=candidateage
        
    def checkagelimit(self):
        if 18<self.joinage<25:
            return True
        else:
            return False