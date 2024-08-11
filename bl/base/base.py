from dal.text_mange_file import Managefile
from common.book import Book

class BookBl:
    def __init__(self) -> None:
        self._dal_book=Managefile(filepath=r"file/book.txt")
        self._list_book: list[Book]=self._dal_book.load_book_data()
        
    def get_list(self):
        return self._list_book
    
    def __validation(self):
        return True
    def creat(self,book:Book):
        if self.__validation():
            print("step1")
            res=self._dal_book.save_book(book,mode='a',write_state="wr")
            return res

    def update(self,book:Book):
        if self.__validation(book):
            self._dal_book.save_book(book)

    def delete(self,book:Book):
        if self.__validation(book):
            self._dal_book.save_book(book)
    

        


        
        
   

