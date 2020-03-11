def sort_list_integers(iterable = None, ascending = True):
	if iterable is None:
		return []
	if len(iterable) is 1:
		return iterable
	if iterable.count(iterable[0]) == len(iterable):
		return iterable
	# if all(isinstance(n,int) for n in iterable) !=  True:
	# 	raise ValueError('List elements different from integers')
	# if all(isinstance(n,float) for n in iterable) !=  True:
	# 	raise ValueError('List elements different from floats')
	
	return iterable

def my_sort(iterable = None, ascending = True, key = None):
	pass

if __name__ == '__main__':
	pass

