import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Scrollbar, Treeview

from bl.base.base import BookBl
from common.book import Book
from common.status import Status
from ui.formbase import BaseForm


class BookForm(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self._book_bl=BookBl()
        self._initial()
        self._on_show()
    

    def _on_show(self):
        self._refresh_book()
  
    def _refresh_book(self):
        for row_book in self.__book_grid.get_children():
            self.__book_grid.delete(row_book)
        book:Book
        print(self._book_bl.get_list())
        res=self._book_bl.get_list()
        for book in self._book_bl.get_list():
                # self.__book_grid.insert("","end",values=(book.title,book.year,book.price,book.isbn,book.pages,book.dec,))
            pass



    def _initial(self):
        self.title("book form")
        self.geometry("600x600")
        # self.resizable(width=False,height=False)
        # self._book_bl=BookBl()
        
        #region headerframe
        self._header=tk.Frame(master=self,height=15,bg="white")
        self._header.pack(side=tk.TOP,fill=tk.X)
        self._header.propagate(False)
        #endregion

        #region footerframe
        self._footer=tk.Frame(master=self,height=80,bg="blue")
        self._footer.pack(side=tk.BOTTOM,fill=tk.X)
        self._footer.propagate(False)
        #endregion
        
        #region body
        self._body=tk.Frame(master=self,bg="white")
        self._body.pack(fill=tk.BOTH,expand=True)
        self._body.propagate(False)
        
        #endregion

        #region add buttun
        btn_add=tk.Button(master=self._footer,text="add",font=("titer",12,"bold"),bg="green",width=7,height=2
                           ,command=self._add_btn_click)
        btn_add.pack(side=tk.LEFT,padx=(6,0),pady=7)
        #endregion

        #region edit buttun
        btn_edit=tk.Button(master=self._footer,text="edit",font=("titer",12,"bold"),bg="green",width=7,height=2
                           ,command=self._edit_btn_click)
        btn_edit.pack(side=tk.LEFT,padx=(6,0),pady=7)
        #endregion

        #region remove buttun
        btn_remove=tk.Button(master=self._footer,text="remove",font=("titer",12,"bold"),bg="green",width=7,height=2
                           ,command=self._remove_btn_click)
        btn_remove.pack(side=tk.LEFT,padx=(6,0),pady=7)
        #endregion

        #region back buttun
        btn_back=tk.Button(master=self._footer,text="back",font=("titer",12,"bold"),bg="yellow",width=7,height=2
                           ,command=self._back_btn_click)
        btn_back.pack(side=tk.RIGHT,padx=(0,6),pady=7)
        #endregion

        #region treeviwe
        self.__book_grid=Treeview(master=self._body,columns=("title","year","price","isbn","pages","dec"),
                                  show="headings",selectmode="extended")
        col_with=self.__book_grid.winfo_width()
        self.__book_grid.column(column="title",anchor="center",width=col_with)
        self.__book_grid.column(column="year",anchor="center",width=col_with)
        self.__book_grid.column(column="price",anchor="center",width=col_with)
        self.__book_grid.column(column="isbn",anchor="center",width=col_with)
        self.__book_grid.column(column="pages",anchor="center",width=col_with)
        self.__book_grid.column(column="dec",anchor="center",width=col_with)

        self.__book_grid.heading(column="title",anchor="center",text="title")
        self.__book_grid.heading(column="year",anchor="center",text="year")
        self.__book_grid.heading(column="price",anchor="center",text="price")
        self.__book_grid.heading(column="isbn",anchor="center",text="isbn")
        self.__book_grid.heading(column="pages",anchor="center",text="pages")
        self.__book_grid.heading(column="dec",anchor="center",text="dec")
        
        self.__book_grid.pack(fill="both",expand=True)
        #endregion

        #region verscrobar
        self.__verscrlbar=Scrollbar(master=self.__book_grid,orient="vertical")
        self.__verscrlbar.pack(side=tk.RIGHT,fill=tk.Y)

        self.__book_grid.configure(yscrollcommand=self.__verscrlbar.set)
        self.__verscrlbar["command"]=self.__book_grid.yview
        #endregion

        #region horscrobar
        self.__horscrlbar=Scrollbar(master=self.__book_grid,orient="horizontal")
        self.__horscrlbar.pack(side=tk.BOTTOM,fill=tk.X)

        self.__book_grid.configure(xscrollcommand=self.__horscrlbar.set)
        self.__horscrlbar["command"]=self.__book_grid.xview
        #endregion
        


    

    def _back_btn_click(self):
        self.destroy()
    

    def _edit_btn_click(self):
        pass

    def _remove_btn_click(self):
        pass

    def _add_btn_click(self):
        self._base_form=BaseForm(book_bl=None,actionform=None)
        self._base_form.mainloop()