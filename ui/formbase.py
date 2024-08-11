import tkinter as tk
from tkinter import messagebox

from bl.base.base import BookBl
from common.book import Book
from common.status import FormAction, Status


class BaseForm(tk.Tk):
    def __init__(self,book_bl:Book,actionform:FormAction) -> None:
        super().__init__()
        self._book_bl=book_bl
        self._actionform=actionform
        self._initial()

    def _initial(self):
        self.title("main form")
        self.geometry("600x600")
        # self.resizable(width=False,height=False)
        
        
        #region headerframe
        self._header=tk.Frame(master=self,height=80,bg="green")
        self._header.pack(side=tk.TOP,fill=tk.X)
        self._header.propagate(False)
        #endregion

        #region footerframe
        self._footer=tk.Frame(master=self,height=80,bg="blue")
        self._footer.pack(side=tk.BOTTOM,fill=tk.X)
        self._footer.propagate(False)
        #endregion
        
        #region body
        self._body=tk.Frame(master=self,bg="red")
        self._body.pack(fill=tk.BOTH,expand=True)
        self._body.propagate(False)
        
        self._info_frame=tk.Frame(master=self._body,height=240,bg="white")
        self._info_frame.pack(side=tk.TOP,fill=tk.X)
        self._info_frame.propagate(False)

        self._rightbody=tk.Frame(master=self._info_frame,bg="white")
        self._rightbody.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)
        self._rightbody.propagate(False)

        self._leftbody=tk.Frame(master=self._info_frame,bg="white")
        self._leftbody.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)
        self._leftbody.propagate(False)

        self._title_frame=tk.Frame(master=self._leftbody,height=80,bg="white")
        self._title_frame.pack(side=tk.TOP,fill=tk.X)
        self._title_frame.propagate(False)

        self._year_frame=tk.Frame(master=self._leftbody,height=80,bg="white")
        self._year_frame.pack(side=tk.TOP,fill=tk.X)
        self._year_frame.propagate(False)

        self._price_frame=tk.Frame(master=self._leftbody,height=80,bg="white")
        self._price_frame.pack(side=tk.TOP,fill=tk.X)
        self._price_frame.propagate(False)

        self._isbn_frame=tk.Frame(master=self._rightbody,height=80,bg="white")
        self._isbn_frame.pack(side=tk.TOP,fill=tk.X)
        self._isbn_frame.propagate(False)

        self._pages_frame=tk.Frame(master=self._rightbody,height=80,bg="white")
        self._pages_frame.pack(side=tk.TOP,fill=tk.X)
        self._pages_frame.propagate(False)

        self._genres_frame=tk.Frame(master=self._rightbody,height=80,bg="white")
        self._genres_frame.pack(side=tk.TOP,fill=tk.X)
        self._genres_frame.propagate(False)

       #endregion

        #region dec
        self._dec=tk.Frame(master=self._body,bg="white",height=240)
        self._dec.pack(side=tk.TOP,fill=tk.X)
        self._dec.propagate(False)

        #endregion

        #region tilte
        self._title_text=tk.Label(master=self._title_frame,text="title:",font=("tahoma",12,"bold"),bg="white")
        self._title_text.pack(side=tk.LEFT)

        self._title_entry=tk.Entry(master=self._title_frame,font=("tahoma",11,"normal"),bg="light gray")
        self._title_entry.pack(fill=tk.BOTH,expand=True,padx=(0,10),pady=20)
        #endregion

        #region year
        self._year_text=tk.Label(master=self._year_frame,text="year:",font=("tahoma",12,"bold"),bg="white")
        self._year_text.pack(side=tk.LEFT)

        self._year_entry=tk.Entry(master=self._year_frame,font=("tahoma",11,"normal"),bg="light gray")
        self._year_entry.pack(fill=tk.BOTH,expand=True,padx=(0,10),pady=20)
        #endregion

        #region price
        self._price_text=tk.Label(master=self._price_frame,text="price:",font=("tahoma",12,"bold"),bg="white")
        self._price_text.pack(side=tk.LEFT)

        self._price_entry=tk.Entry(master=self._price_frame,font=("tahoma",11,"normal"),bg="light gray")
        self._price_entry.pack(fill=tk.BOTH,expand=True,padx=(0,10),pady=20)
        #endregion

        #region isbn
        self._isbn_text=tk.Label(master=self._isbn_frame,text="isbn:",font=("tahoma",12,"bold"),bg="white")
        self._isbn_text.pack(side=tk.LEFT)

        self._isbn_entry=tk.Entry(master=self._isbn_frame,font=("tahoma",11,"normal"),bg="light gray")
        self._isbn_entry.pack(fill=tk.BOTH,expand=True,padx=(0,10),pady=20)
        #endregion

        #region pages
        self._pages_text=tk.Label(master=self._pages_frame,text="pages:",font=("tahoma",12,"bold"),bg="white")
        self._pages_text.pack(side=tk.LEFT)

        self._pages_entry=tk.Entry(master=self._pages_frame,font=("tahoma",11,"normal"),bg="light gray")
        self._pages_entry.pack(fill=tk.BOTH,expand=True,padx=(0,10),pady=20)
        #endregion

        #region genres
        self._genres_text=tk.Label(master=self._genres_frame,text="genres:",font=("tahoma",12,"bold"),bg="white")
        self._genres_text.pack(side=tk.LEFT)

        self._genres_ch1=tk.Checkbutton(master=self._genres_frame,text="comedy",font=("tahoma",11,"bold"),onvalue=1,offvalue=0,bg="white")
        self._genres_ch1.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=(0,10),pady=20)

        self._genres_ch2=tk.Checkbutton(master=self._genres_frame,text="Romantic",font=("tahoma",11,"bold"),onvalue=1,offvalue=0,bg="white")
        self._genres_ch2.pack(fill=tk.BOTH,expand=True,padx=(0,10),pady=20)


        #endregion
       
        #region dec
        self._dec_text=tk.Label(master=self._dec,text="description:",font=("tahoma",12,"bold"),bg="white",anchor="nw")
        self._dec_text.pack(side=tk.TOP,fill=tk.X)

        self._dec_entry=tk.Text(master=self._dec,font=("tahoma",11,"normal"),bg="light gray")
        self._dec_entry.pack(fill=tk.BOTH,expand=True,padx=(10,10),pady=5)
        #endregion

        #region save buttun
        btn_save=tk.Button(master=self._footer,text="save",font=("titer",12,"bold"),bg="green",width=7,height=2
                           ,command=self._save_btn_click)
        btn_save.pack(side=tk.LEFT,padx=(6,0),pady=7)
        #endregion

        #region back buttun
        btn_back=tk.Button(master=self._footer,text="back",font=("titer",12,"bold"),bg="yellow",width=7,height=2
                           ,command=self._back_btn_click)
        btn_back.pack(side=tk.RIGHT,padx=(0,6),pady=7)
        #endregion

    def _back_btn_click(self):
        self.destroy()
    
    def __validition(self):
        err_list:list[str]=[]
        if not self._title_entry.get():
            err_list.append("the title is empty")
        if not self._pages_entry.get():
            err_list.append("the pages is empty")
        if not self._isbn_entry.get():
            err_list.append("the isbn empty")
        if not self._year_entry.get():
            err_list.append("the year is empty")
        if not self._price_entry.get():
            err_list.append("the price is empty")
        # pages=self._pages_entry.get()
        # # if isinstance (pages,int):
        # #     err_list.append("the pages not int")
        return err_list
        


    def _save_btn_click(self):
        res=self.__validition()
        if  not res==[]:
            messagebox.showerror("ERROR",res)
        else:
            inst_book=Book(title=self._title_entry.get(),
                           year=self._year_entry.get(),
                           price=self._pages_entry.get(),
                           isbn=self._isbn_entry.get(),                          
                           pages=self._title_entry.get(),
                           dec=self._dec_entry.get("1.0", "end-1c")
                                           
                          )
            print(inst_book)
            res=self._book_bl.creat(inst_book)
            if res[0]==Status.SUCESS:
                messagebox.showinfo("Success","great :)")
            else:
                messagebox.showerror("Error",res[1])

            

class BookForm(BaseForm):
    def __init__(self):
        super().__init__()
        self._initial()
    
    def _initial(self):
        super()._initial()
        self.title("Book form")

        #region headerframe
        self._header=tk.Frame(master=self,height=50,bg="green")
        self._header.pack(side=tk.TOP,fill=tk.X)
        self._header.propagate(False)
        #endregion

        #region footerframe
        self._footer=tk.Frame(master=self,height=50,bg="blue")
        self._footer.pack(side=tk.BOTTOM,fill=tk.X)
        self._footer.propagate(False)
        #endregion
        
        #region body
        self._body=tk.Frame(master=self,bg="red",height=300)
        self._body.pack(fill=tk.BOTH)
        self._body.propagate(False)
        #endregion
        