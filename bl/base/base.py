from typing import Any
from dal.text_mange_file import Managefile
from common.book import Book
from common.status import MethodResult

class BookBl:
    def __init__(self) -> None:
        self._dal_book=Managefile(filepath=r"file/book.txt")
        self._list_book: list[Book]=[]
        res=self._dal_book.load_data()
        if res.sucess:
            for item in res.result:
                dict=eval(item.strip())
                print(type(dict))
                print(dict)
                self._list_book.append(Book(title=dict["title"],year=dict["year"],price=dict["price"],isbn=dict["isbn"],pages=dict["pages"],dec=dict["dec"]))
               
    def get_list(self):
        return self._list_book
    
    def __validation(self):
        return True
    def creat(self,book:Book):
        if self.__validation():
            print("step1")
            res=self._dal_book.save_data(book,mode='a',write_state="wr")
            return res

    def update(self,book:Book):
        if self.__validation(book):
            self._dal_book.save_data(book)

    def delete(self,book:Book):
        if self.__validation(book):
            self._dal_book.save_data(book)
    

     

        


        
        
   

