
class Book():
    def __init__(self,title:str,year:int,price:float,isbn:str,pages:int,dec:str) -> None:
        self.title=title
        self.year= year
        self.price=price
        self.isbn=isbn
        self.pages=pages
        self.dec=dec

    def __str__(self) -> str:
        dict_book={
        "title":self.title,
        "year":self.year, 
        "price":self.price,
        "isbn":self.isbn,
        "pages":self.pages,
        "dec":self.dec
        }
        return f"{dict_book}"
        
    
    #region property
    @property 
    def title (self) -> int:
        return self.__title
    @title.setter
    def title(self,title:str):
        self.__title=title

    @property 
    def year (self) -> int:
        return self.__year
    @year.setter
    def year(self,year:int):
        self.__year=year

    @property 
    def isbn (self)->str:
        return self.__isbn
    @isbn.setter
    def isbn(self,isbn:str):
        self.__isbn=isbn
      
    @property 
    def pages (self)->int:
        return self.__pages
    @pages.setter
    def pages(self,pages:int):
        self.__pages=pages

    @property
    def price(self)->float:
        return self.__price
    @price.setter
    def price(self,price:float):
        self.__price= price


    @property 
    def dec (self)->str:
        return self.__dec
    @dec.setter
    def dec(self,dec:str):
        self.__dec=dec
    #endregion
    
    
   