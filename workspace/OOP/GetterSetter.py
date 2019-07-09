class Book():
    
    def __init__(self,name):
        self.__name=name
        
    @property
    def bookname(self):
        return self.__name
    
    @bookname.setter
    def bookname(self,new_name):
        self.__name=new_name

book1=Book("Harry Potter")
print(book1.bookname)
book1.bookname="Jungle Book"
print(book1.bookname)