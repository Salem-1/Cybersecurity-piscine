import sys

def	close_with_error_messege():
	print("""incorrect input, the program works as follows:\n
   ./spider [-rlp] URL
   -r : recursively downloads the images in a URL received as a parameter.
   -r -l [N] : indicates the maximum depth level of the recursive download. If not indicated, it will be 5.
   -p [PATH] : indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used.\n""", file=sys.stderr)
	exit(1)

def get_ready_params(r=False, l=0, p='./data/', url=''):
	params = {'r': r, 
		   	  'l': l, 
			  'p': p, 
			  'url': url}
	return params


def	is_Invalid_arg_input(args, len_args):
	if len_args > 5 or len_args < 2 or args[0] != "./spider":
		return True 
	return False


def	is_r_or_rl(args, len_args):
	if len_args == 3 and (args[1] == "-r" or args[1] == "-rl" or args[1] == "-lr"):
		return True 
	return False

def	is_p(args, len_args):
	if len_args == 4 and args[1] == "-p" and args[2] != "" and args[2] != "-r" \
		and args[2] != "-l":
		return True
	return False

def is_rl_no_number(args, len_args):
	if (len_args == 4 and (args[1] == "-r" and args[2] == "-l")) or \
	   	(args[1] == "-l" and args[2] == "-r"):
		return True
	return False
def is_rl_with_number(args, len_args):
	if (len_args == 5 and args[1] == "-r" and args[2] == "-l" and args[3].isdigit()):
		return True
	return False
def is_lr_with_number(args, len_args):
	if (len_args == 5 and args[1] == "-l" and args[2].isdigit() and args[3] == "-r" ):
		return True
	return False




def is_pr(args, len_args):
	if len_args == 5 and args[1] == "-p" and args[2] != "-r" \
		and args[2] != "-l"and args[3] == "-r" :
		return True
	return False 

def is_rp(args, len_args):
	if len_args == 5 and args[1] == "-r" and args[2] == "-p" and args[3] != "-r" \
		and args[3] != "-l" :
		return True
	return False 

def is_valid_single_rlp_compinations(args, len_args):
	if is_r_or_rl(args, len_args)  \
		or is_p(args, len_args):
		return True
	return False

def is_valid_douple_rlp_compinations(args, len_args):
	if is_rl_with_number(args, len_args) or is_rl_no_number(args, len_args) \
		or  is_lr_with_number(args, len_args) or is_pr(args, len_args) or is_rp(args, len_args):
		return True
	return False