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
	if len_args > 7 or len_args < 2 or args[0] != "./spider":
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
	if len_args == 4 and ((args[1] == "-r" and args[2] == "-l") or \
	   	(args[1] == "-l" and args[2] == "-r")):
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
def	is_rp_no_sep(args, len_args):
	if len_args == 4 and args[1] == "-rp" and args[2] != "-l" and args[2] != "-r":
		return True
	return False

def is_prl_all_sep_no_number(args, len_args):
	if len_args == 6 and args[1] == "-p" and args[3] == "-r" and args[4] == "-l":
		return True
	return False
def is_prl_all_sep_with_number(args, len_args):
	if len_args == 7 and args[1] == "-p" and args[3] == "-r" and args[4] == "-l" \
		and args[5].isdigit() and int(args[5]) > -1:
		return True
	return False

def is_prl_with_rl_no_number(args, len_args):
	if len_args == 5 and args[1] == "-p" and (args[3] == "-rl" or args[3] == "-lr"):
		return True
	return False

def is_prl_with_rl_with_number(args, len_args):
	if len_args == 6 and args[1] == "-p" and (args[3] == "-rl" or args[3] == "-lr") \
		  and args[4].isdigit() and int(args[4]) > -1:
		return True
	return False

def is_rlp_number(args, len_args):
	if len_args == 5 and args[1] == "-rlp" and args[2].isdigit() and int(args[2]) > -1:
		return True
	return False 

def is_rpl_number(args, len_args):
	if len_args == 5 and args[1] == "-rpl" and args[3].isdigit() and int(args[3]) > -1:
		return True
	return False 

def is_rlp_no_number(args, len_args):
	if len_args == 4 and (args[1] == "-rpl" or args[1] == "-rlp") and (not args[2].isdigit()):
		return True
	return False 
	
def is_rl_p_no_number(args, len_args):
	if len_args == 5 and args[1] == "-rl" and args[2] == "-p":
		return True
	return False

def is_rl_lr_p_number(args, len_args):
	if len_args == 6 and (args[1] == "-rl" or args[1] == "-lr") \
		 and args[2].isdigit() and int(args[2]) > -1 and args[3] == "-p":
		return True
	return False
def is_r_lp_with_number(args, len_args):
	if len_args == 6 and args[1] == "-r" and args[2] == "-lp" and args[3].isdigit() \
		and int(args[3]) > -1:
		return True
	return False
def is_r_lp_pl_no_number(args, len_args):
	if len_args == 5 and args[1] == "-r" and (args[2] == "-lp" or args[2] == "-pl"):
		return True
	return False

def is_r_pl_with_number(args, len_args):
	if len_args == 6 and args[1] == "-r" and args[2] == "-pl" and args[4].isdigit() \
		and int(args[4]) > -1:
		return True
	return False
def is_r_l_p_no_number(args, len_args):
	if len_args == 6 and args[1] == "-r" and args[2] == "-l" and args[3] == "-p":
		return True
	return False
def is_r_l_p_with_number(args, len_args):
	if len_args == 7 and args[1] == "-r" and args[2] == "-l" and args[4] == "-p" \
		and args[3].isdigit() and int(args[3]) > -1:
		return True
	return False

def is_lrp_no_number(args, len_args):
	if len_args == 4 and (args[1] == "-lrp" or args[1] == "-lpr"):
		return True
	return False
def is_lrp_with_number(args, len_args):
	if len_args == 5 and args[1] == "-lrp" and args[2].isdigit() and int(args[2]) > -1:
		return True
	return False
def is_lpr_with_number(args, len_args):
	if len_args == 5 and args[1] == "-lpr" and args[3].isdigit() and int(args[3]) > -1:
		return True
	return False
def is_r_p_l_with_number(args, len_args):
	if len_args == 7 and args[1] == "-r" and args[2] == "-p" and args[4] == "-l" \
		and args[5].isdigit() and int(args[5]) > -1:
		return True
	return False
def is_valid_single_rlp_compinations(args, len_args):
	if is_r_or_rl(args, len_args)  \
		or is_p(args, len_args):
		return True
	return False

def is_l_rp_pr_no_number(args, len_args):
	if len_args == 5 and args[1] == "-l" and (args[2] == '-rp' or args[2] == '-pr'):
		return True
	return False

def is_l_r_p_no_number(args, len_args):
	if len_args == 6 and args[1] == "-l" and args[2] == '-r' and args[3] == '-p':
		return True
	return False

def is_l_rp_with_number(args, len_args):
	if len_args == 6 and args[1] == "-l" and  args[2].isdigit() and int(args[2]) > -1 \
		and (args[3] == '-rp' or args[3] == '-pr'):
		return True
	return False

def is_l_r_p_with_number(args, len_args):
	if len_args == 7 and args[1] == "-l" and  args[2].isdigit() and int(args[2]) > -1 \
		and args[3] == '-r' and args[4] == '-p':
		return True
	return False

def is_l_p_r_with_number(args, len_args):
	if len_args == 7 and args[1] == "-l" and  args[2].isdigit() and int(args[2]) > -1 \
		and args[3] == '-p' and args[5] == '-r':
		return True
	return False
def is_l_p_r_no_number(args, len_args):
	if len_args == 6 and args[1] == "-l"  \
		and args[2] == '-p' and args[4] == '-r':
		return True
	return False
def is_valid_douple_rlp_compinations(args, len_args):
	if is_rl_with_number(args, len_args) or is_rl_no_number(args, len_args) \
		or  is_lr_with_number(args, len_args) or is_pr(args, len_args) or is_rp(args, len_args)\
			or is_rp_no_sep(args, len_args):
		return True
	return False

def is_valid_triple_rlp_compinations(args, len_args):
	if is_prl_all_sep_no_number(args, len_args) or is_prl_all_sep_with_number(args, len_args) \
		or is_prl_with_rl_no_number(args, len_args) or is_prl_with_rl_with_number(args, len_args) \
		or is_rlp_number(args, len_args) or is_rpl_number(args, len_args) \
		or is_rlp_no_number(args, len_args) or is_rl_p_no_number(args, len_args) \
		or is_rl_lr_p_number(args, len_args) or is_r_lp_with_number(args, len_args) \
		or is_r_lp_pl_no_number(args, len_args) or is_r_pl_with_number(args, len_args) \
		or is_r_p_l_with_number(args, len_args) or is_r_l_p_with_number(args, len_args) \
		or is_r_l_p_no_number(args, len_args) or  is_lrp_no_number(args, len_args) \
		or is_lrp_with_number(args, len_args) or is_lpr_with_number(args, len_args) \
		or is_l_rp_pr_no_number(args, len_args) or is_l_rp_with_number(args, len_args) \
		or is_l_r_p_no_number(args, len_args) or is_l_r_p_with_number(args, len_args) \
		or is_l_p_r_no_number(args, len_args) or is_l_p_r_with_number(args, len_args):
		return True
	return False