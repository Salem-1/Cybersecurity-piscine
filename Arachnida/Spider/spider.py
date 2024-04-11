#!/usr/bin/python3
import sys

#Try break the program then put all of it in trycatch

def	close_with_error_messege():
	print("incorrect input, the program works as follows:\n./spider [-rlp] [domain]", file=sys.stderr)
	exit(1)

def has_worng_args_input(args):
	len_args = len(args)
	if len_args > 5 or len_args < 2 or args[0] != "./spider":
		return True
	if (len_args == 3 and args[1] == "-r" or args[1] == "-rl" or args[1] == "-lr")  \
		or (len_args == 4 and args[1] == "-p" and args[2] != "") \
		or (len_args == 5 and args[1] == "-r" and \
			(args[2] == "-l" and args[3].isdigit() and int(args[3]) > -1)) \
		or(len_args == 4 and args[1] == "-r" and args[2] == "-l") :
		return False
	elif (len_args == 4 and args[1] == "-l" and args[2] == "-r") or \
		 (len_args == 5 and args[1] == "-l" and args[2].isdigit() and int(args[2]) > -1 and args[3] == "-r"):
		return False
	return True
	
def	fill_params(args):
	len_args = len(args)
	params = {'r': False, 
		   	  'l': 0, 
			  'p': './data/', 
			  'url': '',}
	if len_args == 3 and (args[1] == "-r" or args[1] == "-rl" or args[1] == "-lr"):
		params['r'] = True
		params['l'] = 5
		params['url'] = args[2]
	elif len_args == 4 and args[1] == "-p":
		params['p'] = args[2]
		params['url'] = args[3]
	elif (len_args == 4 and (args[1] == "-r" and args[2] == "-l") or \
	   	args[1] == "-l" and args[2] == "-r"):
		params['r'] = True
		params['l'] = 5
		params['url'] = args[3]
	elif (len_args == 5 and args[1] == "-r" and args[2] == "-l" and args[3].isdigit()):
		params['r'] = True
		params['l'] = int(args[3])
		params['url'] = args[4]
	elif (len_args == 5 and args[1] == "-l" and args[2].isdigit() and args[3] == "-r" ):
		params['r'] = True
		params['l'] = int(args[2])
		params['url'] = args[4]
	
	return params


def	parse_spider_args(args):
	return (fill_params(args))


def main():
	if  has_worng_args_input(sys.argv):
		close_with_error_messege()
	print(len(parse_spider_args(sys.argv)))







# 

if __name__ == "__main__":
	main()