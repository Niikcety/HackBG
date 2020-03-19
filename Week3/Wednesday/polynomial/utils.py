

def from_string_to_list_of_terms(poly):
	# allowed only ints, x, ^ and +
	lst = poly.split('+')
	for i in lst:
		for char in i: 
			if not char.isdigit() and not char == 'x' and not char == '^' and not char == '+' and not char == ' ':
				raise TypeError('Forbidden sign')
	return lst

def validate_term(term):
	for i in range(0,len(term)-1):
		if term[i:i+2] == '^x':
			raise TypeError('Invalid ^x')
		elif term[i] == 'x' and term[i+1].isdigit():
			raise TypeError('Invalid pow without ^')
		
	return True

def get_coeficient(term):
	if validate_term(term):
		coef = ''
		for i in term:
			if i == ' ':
				continue
			elif i.isdigit():
				coef += i
			else:
				if coef == '':
					return 1
				else:
					return int(coef)
		# case when term is last input
		return int(coef)


def get_pow(term):
	if validate_term(term):
		power = ''
		if 'x' in term and not '^' in term:
			return 1
		if not 'x' in term and not '^' in term:
			return 0
		else:
			splitted = term.split('^')
			for i in splitted[1]:
				if i.isdigit():
					power += i
			return int(power)


def refactor(der):
	new_der = der[::-1]
	
	for i in range(0,len(new_der)):
		if new_der[i] == ' ':
			continue
		elif new_der[i] == '+':
			return der[0:len(der)-i-1]
		else:
			return der
