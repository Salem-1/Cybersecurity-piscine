from low_level import *

def has_worng_args_input(args):
	len_args = len(args)
	if is_Invalid_arg_input(args, len_args):
		return True
	if is_valid_single_rlp_compinations(args, len_args) :
		return False
	if is_valid_douple_rlp_compinations(args, len_args):
		return False
	if is_valid_triple_rlp_compinations(args, len_args):
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
	elif is_rp_no_sep(args, len_args):
		return get_ready_params(r=True, p=args[2], url=args[3])
	elif is_prl_all_sep_no_number(args, len_args):
		return get_ready_params(r=True, l=5, p=args[2], url=args[5])
	elif is_prl_all_sep_with_number(args, len_args):
		return get_ready_params(r=True, l=int(args[5]), p=args[2], url=args[6])
	elif is_prl_with_rl_no_number(args, len_args):
		return get_ready_params(r=True, l=5, p=args[2], url=args[4])
	elif is_prl_with_rl_with_number(args, len_args):
		return get_ready_params(r=True, l=int(args[4]), p=args[2], url=args[5])
	elif is_rlp_number(args, len_args):
		return get_ready_params(r=True, l=int(args[2]), p=args[3], url=args[4])
	elif is_rpl_number(args, len_args):
		return get_ready_params(r=True, l=int(args[3]), p=args[2], url=args[4])
	elif is_rlp_no_number(args, len_args):
		return get_ready_params(r=True, l=5, p=args[2], url=args[3])
	elif is_rl_p_no_number(args, len_args):
		return get_ready_params(r=True, l=5, p=args[3], url=args[4])
	elif is_rl_lr_p_number(args, len_args):
		return get_ready_params(r=True, l=int(args[2]), p=args[4], url=args[5])
	elif is_r_lp_with_number(args, len_args):
		return get_ready_params(r=True, l=int(args[3]), p=args[4], url=args[5])
	elif is_r_lp_pl_no_number(args, len_args):
		return get_ready_params(r=True, l=5, p=args[3], url=args[4])
	elif is_r_pl_with_number(args, len_args):
		return get_ready_params(r=True, l=int(args[4]), p=args[3], url=args[5])
	elif is_r_p_l_with_number(args, len_args):
		return get_ready_params(r=True, l=int(args[5]), p=args[3], url=args[6])
	elif is_r_l_p_with_number(args, len_args):
		return get_ready_params(r=True, l=int(args[3]), p=args[5], url=args[6])
	elif is_r_l_p_no_number(args, len_args):
		return get_ready_params(r=True, l=5, p=args[4], url=args[5])
	elif is_lrp_no_number(args, len_args):
		return get_ready_params(r=True, l=5, p=args[2], url=args[3])
	elif is_lrp_with_number(args, len_args):
		return get_ready_params(r=True, l=int(args[2]), p=args[3], url=args[4])
	elif is_lpr_with_number(args, len_args):
		return get_ready_params(r=True, l=int(args[3]), p=args[2], url=args[4])
	elif is_l_rp_pr_no_number(args, len_args):
		return get_ready_params(r=True, l=5, p=args[3], url=args[4])
	elif is_l_rp_with_number(args, len_args):
		return get_ready_params(r=True, l=int(args[2]), p=args[4], url=args[5])
	elif is_l_r_p_no_number(args, len_args):
		return get_ready_params(r=True, l=5, p=args[4], url=args[5])
	elif is_l_r_p_with_number(args, len_args):
		return get_ready_params(r=True, l=int(args[2]), p=args[5], url=args[6])
	elif is_l_p_r_with_number(args, len_args):
		return get_ready_params(r=True, l=int(args[2]), p=args[4], url=args[6])
	elif is_l_p_r_no_number(args, len_args):
		return get_ready_params(r=True, l=5, p=args[3], url=args[5])
	else:
		close_with_error_messege()

