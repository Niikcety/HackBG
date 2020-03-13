def the_largest_common_divisor(nominator = 0,denominator = 1):
	if denominator == 0:
		raise ValueError('Forbidden division on zero')
	elif nominator == 0:
		return 1
	else:
		for i in range(1,min(nominator,denominator)+1):
			if nominator % i == 0 and denominator % i == 0:
				tlcd = i
	return tlcd 



def simplify_fraction(arg):
	if isinstance(arg,int):
		raise ValueError('Tuple with one element from type Integer')
	if len(arg) > 2:
		raise ValueError('Tuple with more than two elements')
	elif len(arg) == 2:
		nominator,denominator = arg
		if not isinstance(nominator,int) or not isinstance(denominator,int):
			raise ValueError('Tuple with elements different from integers')
		else:
			new_nominator = abs(nominator)
			new_denominator = abs(denominator)
			tlcd = the_largest_common_divisor(new_nominator,new_denominator)
			return (nominator//tlcd,denominator//tlcd)
	else:
		raise ValueError('Tuple with elements less than two')


if __name__ == '__main__':
	pass