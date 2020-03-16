
def list_checker(fractions):
	if not isinstance(fractions,list):
		raise ValueError("Given argument is not a list")
	for fraction in fractions:
		if not isinstance(fraction,tuple):
			raise ValueError("There is an element that is not tuple")
		if len(fraction) != 2:
			raise ValueError("There is an tuple with size different than two")
		if not isinstance(fraction[0],int) or not isinstance(fraction[1],int):
			raise ValueError("There is an tuple with elements different than int")

	return True

def sort_list_of_tuples_ascending(fractions):
	if len(fractions) == 1 or len(fractions) == 0:
		return fractions

	for i in range(len(fractions)):
		for j in range(0,len(fractions)-i-1):
			if fractions[j][0] / fractions[j][1]  > fractions[j+1][0] / fractions[j+1][1]:
				fractions[j], fractions[j+1] = fractions[j+1], fractions[j]

	return fractions

def sort_list_of_tuples_descending(fractions):
	return sort_list_of_tuples_ascending(fractions)[::-1] 

def test_if_boolean_is_correct(ascending):
	if not isinstance(ascending, bool):
		raise ValueError("Value different from Boolean")
	else:
		return True

def sort_fractions(fractions, ascending = True):
	if list_checker(fractions) and test_if_boolean_is_correct(ascending):
		if ascending == True:
			return sort_list_of_tuples_ascending(fractions)
		else:
			return sort_list_of_tuples_descending(fractions)


if __name__ == '__main__':
	print(sort_fractions([(2, 3), (1, 2)]))
	print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
	print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)],False))
	print(sort_fractions([(4,5),(4,5),(4,5)]))
	print(sort_fractions([(1,2),(2,4),(3,6)]))