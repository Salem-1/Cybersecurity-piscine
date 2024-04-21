#!/usr/bin/python3
import sys
from parse_spider_args import *
from fetch_images import fetch_all_images
from low_level import *
#Try break the program then put all of it in trycatch


def	parse_spider_args(args):
	return (fill_params(args))

def main():
	try:
		if  has_worng_args_input(sys.argv):
			close_with_error_messege()
		params = parse_spider_args(sys.argv)
		fetch_all_images(params)
	except Exception as e:
		print(e)
		close_with_error_messege()

if __name__ == "__main__":
	main()