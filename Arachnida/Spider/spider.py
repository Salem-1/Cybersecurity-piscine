#!/usr/bin/python3
import sys
from parse_spider_args import *
#Try break the program then put all of it in trycatch


def	parse_spider_args(args):
	return (fill_params(args))

def main():
	if  has_worng_args_input(sys.argv):
		close_with_error_messege()
	print(len(parse_spider_args(sys.argv)))

if __name__ == "__main__":
	main()