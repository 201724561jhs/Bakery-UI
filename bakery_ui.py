import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')

        var = IntVar()

        label1 = Label(window, text="샌드위치 (5000)원")
        self.entry1 = Entry(window)
        label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)


        label2 = Label(window, text="케이크 (20000)원")
        self.entry2 = Entry(window)
        label2.grid(row=1, column=0)
        self.entry2.grid(row=1, column=1)

        btn = Button(window, text="주문하기", command= self.send_order)
        btn.grid(row=2, column=0)

    def send_order(self):

        if (self.entry1.get().isnumeric()==True) and (self.entry2.get().isnumeric()==True):
            if int(self.entry1.get()) > 0 and int(self.entry2.get()) > 0:
                order_text = str(self.name) + ": 샌드위치 (5000원) " + str(self.entry1.get()) + "개, 케이크 (20000원) " + str(self.entry2.get()) + "개"
                self.bakeryView.add_order(order_text)
            elif int(self.entry1.get()) > 0 and int(self.entry2.get()) <= 0:
                order_text = str(self.name) + ": 샌드위치 (5000원) " + str(self.entry1.get()) + "개"
                self.bakeryView.add_order(order_text)
            elif int(self.entry1.get()) <= 0 and int(self.entry2.get()) > 0:
                order_text = str(self.name) + ": 케이크 (20000원) " + str(self.entry2.get()) + "개"
                self.bakeryView.add_order(order_text)

        elif (self.entry1.get().isnumeric() == True) and (self.entry2.get().isnumeric() == False):
            if int(self.entry1.get()) > 0:
                order_text = str(self.name) + ": 샌드위치 (5000원) " + str(self.entry1.get()) + "개"
                self.bakeryView.add_order(order_text)

        elif (self.entry1.get().isnumeric()==False) and (self.entry2.get().isnumeric()==True):
            if int(self.entry2.get()) > 0:
                order_text = str(self.name) + ": 케이크 (20000원) " + str(self.entry2.get()) + "개"
                self.bakeryView.add_order(order_text)








if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
