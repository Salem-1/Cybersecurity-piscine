# test_spider.py

import unittest
from unittest.mock import patch
from io import StringIO
import sys
import spider

class TestMyScript(unittest.TestCase):
	@patch('spider.sys.argv', ['spider', '-l', '-r', '-p', '-r', 'www.example.com'])  # Simulate command-line input
	def test_parse_spider_args_long_input(self):
		captured_output = StringIO()
		with patch('sys.stderr', captured_output):
			with self.assertRaises(SystemExit) as cm:
				spider.main()
		self.assertEqual(cm.exception.code, 1)
		output = captured_output.getvalue().strip()
		self.assertIn("incorrect input", output)
		self.assertIn("./spider [-rlp] [domain]", output)
	
	@patch('spider.sys.argv', ['spider'])  # Simulate command-line input
	def test_parse_spider_args_no_input(self):
		captured_output = StringIO()
		with patch('sys.stderr', captured_output):
			with self.assertRaises(SystemExit) as cm:
				spider.main()
		self.assertEqual(cm.exception.code, 1)
		output = captured_output.getvalue().strip()
		self.assertIn("incorrect input", output)
		self.assertIn("./spider [-rlp] [domain]", output)
	
	@patch('spider.sys.argv', ['not_spider', "www.example.com"])  # Simulate command-line input
	def test_parse_spider_args_no_spider(self):
		captured_output = StringIO()
		with patch('sys.stderr', captured_output):
			with self.assertRaises(SystemExit) as cm:
				spider.main()
		self.assertEqual(cm.exception.code, 1)
		output = captured_output.getvalue().strip()
		self.assertIn("incorrect input", output)
		self.assertIn("./spider [-rlp] [domain]", output)

if __name__ == "__main__":
	unittest.main()
