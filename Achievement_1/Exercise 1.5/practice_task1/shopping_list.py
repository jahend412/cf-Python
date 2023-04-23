class ShoppingList(object):
   # Initialiazation method
    def __init__(self, list_name):
        shopping_list = []
        self.list_name = list_name
        self.shopping_list = shopping_list

     # Method to add new items to self.shopping_list
    def add_item(self, item):
        self.item = item
        if item in self.shopping_list:
            print("Item already in the list")
        else:
            self.shopping_list.append(item)
            print("Item added to the list")

 # Method to remove an item from self.shopping_list.
    def remove_item(self, item):
        self.item = item
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print("Item removed from the list")
        else:
            print("Item not in the list")

 # Method to view the shopping list
    def view_list(self):
        print("Shopping List: ", self.list_name)
        print("---------------")
        for item in self.shopping_list:
            print(item)
