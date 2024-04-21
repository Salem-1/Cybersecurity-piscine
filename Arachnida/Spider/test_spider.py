# test_spider.py

import unittest
from unittest.mock import patch
from io import StringIO
import sys
import spider
import collect_links

#Try break the program then put all of it in trycatch
class TestMyScript(unittest.TestCase):
	@patch('spider.sys.argv', ['./spider', '-l', '-r', '-p', '-r', '-r', '-p' ,'www.example.com'])  # Simulate command-line input
	def test_parse_spider_args_long_input(self):
		captured_output = StringIO()
		with patch('sys.stderr', captured_output):
			with self.assertRaises(SystemExit) as cm:
				spider.main()
		self.assertEqual(cm.exception.code, 1)
		output = captured_output.getvalue().strip()
		self.assertIn("incorrect input", output)
		self.assertIn("/spider [-rlp] URL", output)
	
	@patch('spider.sys.argv', ['./spider'])  # Simulate command-line input
	def test_parse_spider_args_no_input(self):
		captured_output = StringIO()
		with patch('sys.stderr', captured_output):
			with self.assertRaises(SystemExit) as cm:
				spider.main()
		self.assertEqual(cm.exception.code, 1)
		output = captured_output.getvalue().strip()
		self.assertIn("incorrect input", output)
		self.assertIn("./spider [-rlp] URL", output)
	
	@patch('spider.sys.argv', ['not_spider', "www.example.com"])  # Simulate command-line input
	def test_parse_spider_args_no_spider(self):
		captured_output = StringIO()
		with patch('sys.stderr', captured_output):
			with self.assertRaises(SystemExit) as cm:
				spider.main()
		self.assertEqual(cm.exception.code, 1)
		output = captured_output.getvalue().strip()
		self.assertIn("incorrect input", output)
		self.assertIn("./spider [-rlp] URL", output)
	
	def test_parse_spider_r(self):
		args =  ['./spider', '-r',"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
	
	def test_parse_spider_l(self):
		args =  ['./spider', '-r', "-l","www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', "-rl","www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', "-lr","www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-r', "-l", '4', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-r', "-l", 'hala', "www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-r', "-l", '-5', "www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', "-l", '-5', "www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', "-l", "www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', "-l", "-r", "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', "-l", "3" ,"-r", "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
	
	def test_parse_spider_l_param(self):
		args =  ['./spider', '-r', "-l", "www.example.com"]
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['p'], './data/')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		args =  ['./spider', '-r', "-l", "7", "www.example.com"]
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['p'], './data/')
		self.assertEqual(spider.parse_spider_args(args)['l'], 7)
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-l', "-r", "www.example.com"]
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['p'], './data/')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-l', "10" ,"-r", "www.example.com"]
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['p'], './data/')
		self.assertEqual(spider.parse_spider_args(args)['l'], 10)
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
	
	def test_parse_spider_r_param(self):
		args =  ['./spider', '-r',"www.example.com"]
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['p'], './data/')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-rl',"www.example.com"]
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['p'], './data/')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-lr',"www.example.com"]
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['p'], './data/')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')

	
	def test_parse_spider_p(self):
		args =  ['./spider', '-p',"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', " ", "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/saveme',"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
	
	def test_parse_spider_p_param(self):
		args =  ['./spider', '-p', '/saveme',"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 0)
		self.assertFalse(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
	

	def test_parse_spider_pr(self):
		args =  ['./spider', '-rp',"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-pr',"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-r', '-p',"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '-r',"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '-r' ,'/saveme' ,"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '-l' ,"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/svame', '-l' ,"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '-r' ,'-r' , "www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '-l' ,'-r' , "www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-r', '/saveme' ,'-p' , "www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-r', '-p', "www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/saveme' ,'-r' , "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-rp', '/saveme' , "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))

	def test_parse_spider_pr_param(self):
		args =  ['./spider', '-p', '/saveme' ,'-r' , "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 0)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-r', '-p', '/saveme', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 0)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-rp', '/saveme', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 0)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')

	def test_parse_spider_prl(self):
		args =  ['./spider', '-p', '/saveme','-r', '-l','-3',"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/saveme','-r', '-l','nonsense',"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-prl',"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '-r', '-l',"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/saveme','-r', '-l',"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/saveme','-r', '-l','3',"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/saveme','-rl',"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/saveme','-lr',"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/saveme','-lr', 'nonsense' ,"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/saveme','-rl', 'nonsense' ,"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/saveme','-lr', 'nonsense' ,"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/saveme','-rl', '-3' ,"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/saveme','-lr', '-3' ,"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/saveme','-rl', '3' ,"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-p', '/saveme','-lr', '3' ,"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))

	def test_parse_spider_prl_param(self):
		args =  ['./spider', '-p', '/saveme','-r', '-l',"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-p', '/saveme','-rl',"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-p', '/saveme','-lr',"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-p', '/saveme','-r', '-l', '4',"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-p', '/saveme','-rl', '4',"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-p', '/saveme','-lr', '4',"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')

	def test_parse_spider_rlp(self):
		args =  ['./spider', '-rlp',"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-rlp', '4', "www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-rpl', '4', "www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-rlp', '4', '/saveme', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-rpl', '4', '/saveme', "www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-rpl', '/saveme', '4', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-rpl', '/saveme', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-rlp', '/saveme', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-rl', '-p', '/saveme', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-rl', '4','-p', '/saveme', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-lr', '4','-p', '/saveme', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-r', '-lp', '4', '/saveme', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-r', '-lp', '/saveme', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-r', '-pl', '/saveme', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-r', '-pl', '/saveme', '4', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-r', '-p', '/saveme', '-l' ,'4', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-r',  '-l' ,'4','-p', '/saveme', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-r',  '-l' ,'-p', '/saveme', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))

	def test_parse_spider_rlp_param(self):
		args =  ['./spider', '-rlp', '4', '/saveme', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-rpl', '/saveme', '4', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		args =  ['./spider', '-rpl', '/saveme', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-rlp', '/saveme', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-rl', '-p', '/saveme', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-rl', '4','-p', '/saveme', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-lr', '4','-p', '/saveme', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-r', '-lp', '4','/saveme', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-r', '-lp','/saveme', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		args =  ['./spider', '-r', '-pl','/saveme', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-r', '-pl', '/saveme', '4', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-r', '-p', '/saveme', '-l' ,'4', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-r',  '-l' ,'4','-p', '/saveme', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')
		args =  ['./spider', '-r',  '-l' ,'-p', '/saveme', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')

	def test_parse_spider_lrp(self):
		args =  ['./spider', '-lrp',"www.example.com"]
		self.assertTrue(spider.has_worng_args_input(args))
		args =  ['./spider', '-lrp','/saveme' ,"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-lpr','/saveme' ,"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		# args =  ['./spider', '-l', '-r', '-p', '/saveme' ,"www.example.com"]
		# self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-lrp', '4', '/saveme' ,"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-lpr', '/saveme', '4', "www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-l', '-rp', '/saveme' ,"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-l', '-pr', '/saveme' ,"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-l', '4','-pr', '/saveme' ,"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-l', '4','-rp', '/saveme' ,"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-l','-r', '-p', '/saveme' ,"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-l', '4','-r', '-p', '/saveme' ,"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-l', '4','-r', '-p', '/saveme' ,"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))
		args =  ['./spider', '-l', '-p', '/saveme', '-r' ,"www.example.com"]
		self.assertFalse(spider.has_worng_args_input(args))

	def test_parse_spider_lrp_param(self):
		args =  ['./spider', '-lrp','/saveme' ,"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')		
		args =  ['./spider', '-lpr','/saveme' ,"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')		
		args =  ['./spider', '-lrp', '4', '/saveme' ,"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')		
		args =  ['./spider', '-lpr', '/saveme', '4', "www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')		
		args =  ['./spider', '-l', '-rp', '/saveme' ,"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')		
		args =  ['./spider', '-l', '-pr', '/saveme' ,"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')		
		args =  ['./spider', '-l', '4','-pr', '/saveme' ,"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')		
		args =  ['./spider', '-l', '4','-rp', '/saveme' ,"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')		
		args =  ['./spider', '-l','-r', '-p', '/saveme' ,"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')		
		args =  ['./spider', '-l', '4','-r', '-p', '/saveme' ,"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')		
		args =  ['./spider', '-l', '4', '-p', '/saveme', '-r' ,"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 4)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')		
		args =  ['./spider', '-l', '-p', '/saveme', '-r' ,"www.example.com"]
		self.assertEqual(spider.parse_spider_args(args)['p'], '/saveme')
		self.assertEqual(spider.parse_spider_args(args)['l'], 5)
		self.assertTrue(spider.parse_spider_args(args)['r'])
		self.assertEqual(spider.parse_spider_args(args)['url'], 'www.example.com')		

if __name__ == "__main__":
	unittest.main()









