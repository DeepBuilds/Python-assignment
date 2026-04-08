class Library:
    def __init__(self,book_name,author,avability=True):
        self.book_name=book_name
        self.author=author
        self.avability=avability
    def display(self):
    
        if self.avability==True:
            print("book is avala")
        else:
            print("book is not ava")
    def return_book(self):
        self.avability=True
        print("book returned")
    def check_out(self):
        self.book_name=False
        print("book cheakrd")
        
book1=Library("Harrypotter","pandit neharu")
book2=Library("one piece","echiro oda")
book1.display()
book1.check_out()
book2.return_book()

