from typing import Literal
from common.book import Book
from common.status import Status



class Managefile():
    def __init__(self,filepath) -> None:
        self._path=filepath

    def save_book(self, instace:Book|list[Book],
                  mode:Literal["w"]|Literal["a"]="a",
                  write_state:Literal["wr"]|Literal["wl"]="wr"):
        try:
            with open(file=self._path,mode=mode) as file_object:
                if write_state=="wr":
                    file_object.write(str(instace))
                else:
                    file_object.writelines(map(lambda b: str(b),instace))

        except BaseException as err:
            return (Status.ERROR,err)
        else:
            return(Status.SUCESS,None)
        
    
    
    def load_book_data(self):
        try:
            with open(file=self._path,mode="rt") as file_object:
                res=file_object.readlines()
        except BaseException as err:
            raise err
        else:
            return(res)