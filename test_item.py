import unittest
from item import Item

class TestItem(unittest.TestCase):

    def test_item_has_price(self):
        item = Item("unicorn", 100)
        self.assertEqual(
            item.price,
            100
        )

    def test_item_has_name(self):
        item = Item("rainbow", 99)
        self.assertEqual(
            item.name,
            "rainbow"
        )
