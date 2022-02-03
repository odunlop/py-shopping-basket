class ShoppingBasket:
    def __init__(self):
        self.contents = []
    
    def add(self, item):
        self.contents.append(item)
    
    def remove(self, item_name):
        new_contents = [ item for item in self.contents if item.name != item_name ]
        self.contents = new_contents
        # for item in self.contents:
        #     if item.name == item_name:
        #         self.contents.remove(item)