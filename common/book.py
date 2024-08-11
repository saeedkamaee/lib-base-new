
class Book():
    def __init__(self,title,year,price,isbn,pages,dec) -> None:
        self.title=title
        self.year= year
        self.price=price
        self.isbn=isbn
        self.pages=pages
        self.dec=dec

    def __str__(self) -> str:
        return f"title={self.title},year={self.year},price={self.price},isbn={self.isbn},pages={self.pages},dec={self.dec}"

    #region property
    @property 
    def title (self):
        return self.__title
    @title.setter
    def title(self,title):
        self.__title=title

    @property 
    def year (self):
        return self.__year
    @year.setter
    def year(self,year):
        self.__year=year

    @property 
    def isbn (self):
        return self.__isbn
    @isbn.setter
    def isbn(self,isbn):
        self.__isbn=isbn
      
    @property 
    def pages (self):
        return self.__pages
    @pages.setter
    def pages(self,pages):
        self.__pages=pages

    @property 
    def dec (self):
        return self.__dec
    @dec.setter
    def dec(self,dec):
        self.__dec=dec
    #endregion