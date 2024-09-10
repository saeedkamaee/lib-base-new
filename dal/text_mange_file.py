from typing import Any, Literal
from common.book import Book
from common.status import MethodResult



class Managefile():
    def __init__(self,filepath) -> None:
        self._path=filepath

    def save_data(self, instace:Any|list[Any],
                  mode:Literal["w"]|Literal["a"]="a",
                  write_state:Literal["wr"]|Literal["wl"]="wr"):
        try:
            with open(file=self._path,mode=mode) as file_object:
                if write_state=="wr":
                    file_object.write(f"{str(instace)}\n")
                else:
                    file_object.writelines(map(lambda b: f"{str(b)}\n",instace))

        except BaseException as err:
            return (MethodResult(sucess=False,err_mesage=err))
        else: 
            return (MethodResult(sucess=True))
        
    
    
    def load_data(self):
        try:
            with open(file=self._path,mode="rt") as file_object:
                res=file_object.readlines()
        except BaseException as err:
            return (MethodResult(sucess=False,err_mesage=err))
        else: 
            return (MethodResult(sucess=True,result=res))