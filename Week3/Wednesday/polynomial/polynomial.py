import sys
from utils import get_pow, get_coeficient, from_string_to_list_of_terms, refactor

class Term:
	def __init__(self,term):
		self.coef = get_coeficient(term)
		self.pow = get_pow(term)

	def __repr__(self):
		if self.coef == 0:
			return ' '
		if self.pow == 0:
			return f'{self.coef}'
		if self.pow == 1:
			return f'{self.coef}x'
		return f'{self.coef}x^{self.pow}'

	def __str__(self):
		if self.coef == 0:
			return ' '
		if self.pow == 0:
			return f'{self.coef}'
		if self.pow == 1:
			return f'{self.coef}x'
		return f'{self.coef}x^{self.pow}'

	def __eq__(self, other):
		return self.coef == other.coef and self.pow == other.pow


	def get_derivative(self):
		if self.pow == 0:
			return Term(str(0))
		elif self.pow == 1:
			return Term(str(self.coef))
		else:
			term = ''
			term += str(self.coef*self.pow)
			term += 'x'
			if self.pow - 1 > 1:
				term += '^'
				term += str(self.pow - 1)
			return Term(term)


class Polynomial:

	def __init__(self,poly):
		self.polynom = [Term(i) for i in from_string_to_list_of_terms(poly)]
	
	def __repr__(self):
		poly = ''
		for i in self.polynom:
			if i == self.polynom[self.len()-1]:
				poly += str(i)
			else:
				poly += str(i) + ' + '
		return poly

	def __str__(self):
		poly = ''
		for i in self.polynom:
			if i == self.polynom[self.len()-1]:
				poly += str(i)
			else:
				poly += str(i) + ' + '
		return poly 

	def __getitem__(self, index):
		return self.polynom[index]

	def get_poly(self):
		return self.polynom	

	def len(self):
		return len(self.polynom)


class Derivative(Polynomial):
	def __init__(self, poly):
		super().__init__(poly)
		self.derivative = [term.get_derivative() for term in super().get_poly()]

	def __repr__(self):
		der = ''
		for i in self.derivative:
			if i == self.derivative[self.len()-1]:
				der += str(i)
			elif str(i) == ' ':
				continue
			else:
				der += str(i) + ' + '

		return f'The derivative of f(x):{super().__repr__()} is: \nf\'(x):{refactor(der)}'

	def __str__(self):
		der = ''
		for i in self.derivative:
			if i == self.derivative[self.len()-1]:
				der += str(i)
			elif str(i) == ' ':
				continue
			else:
				der += str(i) + ' + '

		return f'The derivative of f(x):{super().__repr__()} is: \nf\'(x):{refactor(der)}'

	def len(self):
		return len(self.polynom)



if __name__ == '__main__':
	der = Derivative('2x^3 + 4')
	print(der)