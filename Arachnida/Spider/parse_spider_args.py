from low_level import *

def has_worng_args_input(args):
	len_args = len(args)
	if is_Invalid_arg_input(args, len_args):
		return True
	if is_valid_single_rlp_compinations(args, len_args) :
		return False
	if is_valid_douple_rlp_compinations(args, len_args):
		return False
	return True

def	fill_params(args):
	len_args = len(args)
	if is_r_or_rl(args, len_args):
		return get_ready_params(r=True, l=5, url=args[2])
	elif is_p(args, len_args):
		return get_ready_params(p=args[2], url=args[3])
	elif is_rl_no_number(args, len_args):
		return get_ready_params(r=True, l=5, url=args[3])
	elif is_rl_with_number(args, len_args):
		return get_ready_params(r=True, l=int(args[3]), url=args[4])
	elif is_lr_with_number(args, len_args):
		return get_ready_params(r=True, l=int(args[2]), url=args[4])
	elif is_pr(args, len_args):
		return get_ready_params(r=True, p=args[2], url=args[4])
	elif is_rp(args, len_args):
		return get_ready_params(r=True, p=args[3], url=args[4])
	else:
		close_with_error_messege()

