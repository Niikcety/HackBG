from simplify_fractions import simplify_fraction

def check_if_list_is_legit(fractions):
	if fractions == []:
		raise ValueError('Empty list')
	else:
		for fraction in fractions:
			if isinstance(fraction,int):
				raise ValueError('Tuple with one element')
			if len(fraction) != 2:
				raise ValueError('Tuples different than two items')

	for fraction in fractions:
		nom, denom = fraction
		if not isinstance(nom,int) or not isinstance(denom,int):
			raise ValueError('Tuple with different elements than int')

	return True

def find_the_total_denominator(fractions):
	denom = 1
	for fraction in fractions:
		nominator,denominator = fraction
		if nominator == 0:
			continue
		elif denominator == 0:
			raise ValueError('Forbidden division of zero')
		else:
			denom *= denominator

	return denom


def return_multiplier(fraction,denominator):
	nom,denom = fraction
	return denominator // denom

def expand_the_fractions(fractions):
	new_list = []
	total_denom = find_the_total_denominator(fractions)
	for fraction in fractions:
		nom,denom = fraction
		if nom == 0:
			continue
		else:
			mult = return_multiplier(fraction,total_denom)
			new_list.append((nom*mult,denom*mult))
	return new_list


def collect_fractions(fractions):
	if check_if_list_is_legit(fractions):
		lst = expand_the_fractions(fractions)
		summ = 0
		for fraction in lst:
			nom,denom = fraction
			summ += nom
		return simplify_fraction((summ,find_the_total_denominator(fractions)))
	

if __name__ == '__main__':
	print(collect_fractions([(1,3),(2,3)]))