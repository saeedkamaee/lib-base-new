from enum import Enum
from typing import Any

class Status(Enum):
    ERROR=0
    SUCESS=1

class FormAction(Enum):
    CREAT=0
    ADD=1
    SAVE=2
    EDIT=3

class FormResault(Enum):
    BACK=0
    SAVE=1

class MethodResult():
    def __init__(self,sucess:bool,err_mesage:BaseException|str|None=None,result:Any|None=None) -> None:
        self.__sucess=sucess
        self.__err_mesage=err_mesage
        self.__result=result
        
    @property 
    def sucess(self)->bool:
        return self.__sucess
    
    @property 
    def err_mesage(self)->BaseException|str|None:
        return self.__err_mesage
    
    @property 
    def result(self)->Any|None:
        return self.__result