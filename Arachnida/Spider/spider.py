#!/usr/bin/python3
import sys

def	close_with_error_messege():
	print("incorrect input, the program works as follows:\n./spider [-rlp] [domain]", file=sys.stderr)
	exit(1)

def	parse_spider_args():
	args = sys.argv
	if len(args) > 5 or len(args) < 2 or args[0] != "spider":
		close_with_error_messege()
	return (args)


def main():
	print(len(parse_spider_args()))







# 

if __name__ == "__main__":
	main()