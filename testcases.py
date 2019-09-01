import unittest
import pandas as pd
from coinchange import generate_data, order_product, pack_product

class TestBakeryOrderForm(unittest.TestCase):

    def test_generate_data(self):
        bakery_goods = generate_data('')

        self.assertEquals(isinstance(bakery_goods, pd.DataFrame), True)
    
    def test_order_product(self):
        self.assertEqual(order_product('10 VS5'), '10 VS5 $17.98:\n\t2 x 5 at $8.99\n')
        self.assertEqual(order_product('14 MB11'), '14 MB11 $54.8:\n\t1 x 8 at $24.95\n\t3 x 2 at $9.95\n')
        self.assertEqual(order_product('13 CF'), '13 CF $25.85:\n\t2 x 5 at $9.95\n\t1 x 3 at $5.95\n')
        self.assertEqual(order_product('ASDF'), 'Invalid input detected. Please try again.')
        self.assertEqual(order_product('10, VS5'), 'Invalid input detected. Please try again.')
        self.assertEqual(order_product('34 VS67'), 'Invalid input detected. Please try again.')
        self.assertEqual(order_product('10, VS5'), '10 VS5 $17.98:\n\t2 x 5 at $8.99\n')

    def test_pack_product(self):
        self.assertEqual(pack_product(10, 'VS5'), '10 VS5 $17.98:\n\t2 x 5 at $8.99\n')
        self.assertEqual(pack_product(14, 'MB11'), '14 MB11 $54.8:\n\t1 x 8 at $24.95\n\t3 x 2 at $9.95\n')
        self.assertEqual(pack_product(13, 'CF'), '13 CF $25.85:\n\t2 x 5 at $9.95\n\t1 x 3 at $5.95\n')
        self.assertEqual(pack_product(13, 'CF'), '14 CF $25.85:\n\t2 x 5 at $9.95\n\t1 x 3 at $5.95\n')
        self.assertEqual(pack_product(100, 'RYS5'), None)
        self.assertEqual(pack_product(15, None), None)

if __name__ == '__main__':
    unittest.main()