import unittest

class bar(unittest.TestCase):
	
	def test_foo(self):
		self.assertEqual('foo', 'foo')
		
		
		
unittest.main()