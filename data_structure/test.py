import unittest
from dataStructure import Stack, parChecker, genParChecker

class TestStack(unittest.TestCase):

	def setUp(self):
		pass
		
	def test_empty(self):
		s = Stack()
		self.assertTrue(s.isEmpty())

	def test_push(self):
		s = Stack()
		s.push('item')
		self.assertEqual(s.items, ['item'])

	def test_pop(self):
		s = Stack()
		s.push('item')
		self.assertEqual(s.pop(), 'item')
		self.assertTrue(s.isEmpty())

	def test_peek(self):
		s = Stack()
		s.push('item')
		self.assertEqual(s.peek(), 'item')
		self.assertFalse(s.isEmpty())
		self.assertEqual(s.items, ['item'])

	def test_size(self):
		s = Stack()
		s.push('item')
		self.assertEqual(s.size(), 1)


class TestParCheck(unittest.TestCase):
	def test_simple_par(self):
		self.assertEqual(parChecker('((()))'), True)
		self.assertEqual(parChecker('((()'), False)
	
	def test_multi_par(self):
		self.assertEqual(genParChecker('{{([][])}()}'), True)
		self.assertEqual(genParChecker('[[{{(())}}]]'), True)
		self.assertEqual(genParChecker('[][][]()(){}{}'), True)
		self.assertFalse(genParChecker('([)]'))
		self.assertFalse(genParChecker('((()]))'))
		self.assertFalse(genParChecker('[{()]'))


if __name__ == "__main__":
	unittest.main()
