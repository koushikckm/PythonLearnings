class Restaurant():
    
    def __kitchen(self):
        print("Please report to kitchen. You are permitted")
        
    def staffmember(self,access):
        if access:
            self.__kitchen()
        else:
            print("You do not have access to kitchen")
            
rest=Restaurant()
staffaccescheck=int(input("Are you a cook? Enter 1 for yes 0 for no"))
rest.staffmember(staffaccescheck)
rest.__kitchen()