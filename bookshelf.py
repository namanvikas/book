class bookshelf:
    
  def __init__(self,name,author,price,published):
    
    self.book_name=name
    self.book_author=author
    self.book_price=price
    self.book_published=published

  def BOOK (self):
       
     print("name:"+self.book_name)
     print("author:"+self.book_author)
     print("price:"+self.book_price)
     print("published:"+self.book_published)
     
bookshelf=BOOK("Harry Potter and the Philosepher stone","J.K Rowling","1,928","1997")
bookshelf.BOOK()


     
     
                     