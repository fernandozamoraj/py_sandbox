import unittest

class TestForFoo(unittest.TestCase):

    def setUp(self):
        self.x = 'setUp'

    def tearDown(self):
        self.x = 'tearDown'

    def test_that_bar(self):
        self.assertEqual('bar', 'bar')

    def test_that_foo(self):
        self.assertEqual('foo', 'foo')
	
    def test_that_foobar(self):
        self.assertFalse('foo' == 'bar')

    def test_that_barbar(self):
        self.assertTrue('bar' == 'bar')        
	
if __name__=='__main__':
    unittest.main()
	