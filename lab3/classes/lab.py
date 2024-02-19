class soda:
    def __init__(self,dobavka):
        self.dobavka=dobavka
    def show_my_drink(self):
        self.dobavka=print(f"газировка и {self.dobavka}")
n=soda(5)
n.show_my_drink()