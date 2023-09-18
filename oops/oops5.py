class Inventory:
    def __init__(self):
        self.items_dict={}
    def add_item(self, item_id,name, count, price):
        self.items_dict[item_id] = {"item-name": name, "stock-count": count, "price": price}
    def update_item(self, item_id, stock_count, price):
        if item_id in self.items_dict:
            self.items_dict[item_id]["stock-count"] = stock_count
            self.items_dict[item_id]["price"] = price
        else:
            print("Item not avilable")
    def check_item(self,id):
        if id in self.items_dict:
            item = self.items_dict[id]
            print("*""Product Name:",item['item-name'],"*","Stock Count:",item['stock-count'],"*","Price:",item['price'])
        else:
            print( "Item is not available")
obj=Inventory()
obj.add_item(457,"chair",74,4880)
obj.add_item(5008,"table",48,8550)
obj.add_item(6303,"dining-table",69,10400)
print("*****************""")
print("ITEM DETAILS")
print(obj.check_item(457))
print("--------------")
print(obj.check_item(5008))
print("--------------")
print(obj.check_item(6303))
print("--------------")
#change the details of item
print("UPDATED ITEM")
obj.update_item(6303,48,12000)
obj.update_item(457,59,13000)
obj.update_item(5008,78,15000)
print(obj.check_item(457))
print(obj.check_item(5008))
print(obj.check_item(6303))
print("CHECK ITEM")
obj.check_item(457)
obj.check_item(6303)
obj.check_item(5008)