import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],     (quote['top_bid']['price'] + quote['top_ask']['price'])/2))
    

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],     (quote['top_bid']['price'] + quote['top_ask']['price'])/2))
    
    


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_PriceBZero(self):
    price_a=116.87
    price_b=0
    self.assertIsNone(getRatio(price_a  ,price_b))

  
    def test_getRatio_PriceAZero(self):
    price_a=0
    price_b=116.87
    self.assertEqual(getRatio(price_a  ,price_b), 0)



  def test_getRatio_greaterThan(self):
    price_a=316.87
    price_b=158.44
    self.assertGreater(getRatio(price_a  ,price_b), 1)

  def test_getRatio_lessThan(self):
    price_a=158.44
    price_b=316.47
    self.assertLess(getRatio(price_a  ,price_b), 1)


  def test_getRatio_exactlyOne(self):
    price_a=116.87
    price_b=116.87
    self.assertEqual(getRatio(price_a  ,price_b), 1)

  
    

  

  

  
    





if __name__ == '__main__':
    unittest.main()

print("Hello")
