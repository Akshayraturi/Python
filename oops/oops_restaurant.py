class Restaurant:
    def __init__(self):
        self.menu_items={}
        self.book_tables=[]
        self.customer_order={}
    def add_item_to_menu(self,item,price):
        self.menu_items[item]=price
    def booktables(self,table):
        self.book_tables.append(table)
    def customer(self,order,table):
        self.customer_order[order]=table
    def print_menu(self):
       for item,price in self.menu_items.items():
        print(item,":",price)
    def print_book(self):
        for table in self.book_tables:
            print(table)
    def print_order(self):
        for order,table in self.customer_order.items():
            print("order:",order,"=","table:",table)

obj=Restaurant()
obj.add_item_to_menu("bread",45)
obj.add_item_to_menu("burger",80)
obj.add_item_to_menu("pizza",90)
obj.add_item_to_menu("french fries",45)
obj.add_item_to_menu("noodles",65)
obj.add_item_to_menu("chicken curry",155)
obj.booktables(1)
obj.booktables(2)
obj.booktables(8)
obj.booktables(89)
obj.booktables(18)
obj.booktables(28)
obj.customer("burger",4)
obj.customer("pizza",9)
obj.customer("noodles",11)
obj.customer("french fries",21)
obj.customer("bread",11)
obj.customer("chicken curry",13)
obj.customer("chicken curry",21)
print("-----------------MENU----------------------")
obj.print_menu()
print("-----------------BOOKED TABLES-------------")
obj.print_book()
print("-----------------CUSTOMER ORDER------------")
obj.print_order()