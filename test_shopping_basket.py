import unittest
from shopping_basket import ShoppingBasket
from item import Item

class TestShoppingBasket(unittest.TestCase):
    def test_add_one_item(self):
        basket = ShoppingBasket()
        item = Item("milk", 2)
        basket.add(item)
        self.assertEqual(basket.contents, [item])
    
    def test_remove_one_item(self):
        basket = ShoppingBasket()
        milk = Item("milk", 2)
        tea = Item("tea", 1)
        basket.add(milk)
        basket.add(tea)
        basket.remove("milk")
        self.assertEqual(basket.contents, [tea])
    
    def test_remove_multiple_same_name_removes_all(self):
        basket = ShoppingBasket()
        milk = Item("milk", 2)
        more_milk = Item("milk", 2)
        basket.add(milk)
        basket.add(more_milk)
        basket.remove("milk")
        self.assertEqual(basket.contents, [])
