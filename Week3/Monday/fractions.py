def greatest_common_divisor(number1, number2):
	divisor = 1
	for i in range(1,min(number1,number2)+1):
		if number1 % i == 0 and number2 % i == 0:
			divisor = i

	return divisor

class Fraction:
	def __init__(self, nom, denom):
		if not isinstance(nom,int) or not isinstance(denom, int):
			raise ValueError('Arguments different than integers')
		elif denom == 0:
			raise ValueError('Denominator cannot be zero')
		else:	
			self.nom = nom
			self.denom = denom

	def __repr__(self):
		return '{}/{}'.format(self.nom, self.denom)

	def __str__(self):
		return '{}/{}'.format(self.nom, self.denom)	

	# self == other
	def __eq__(self, other):
		return self.nom / self.denom == other.nom / other.denom

	# self < other
	def __lt__(self, other):
		return self.nom / self.denom < other.nom / other.denom
	
	# self > other
	def __gt__(self, other):
		return self.nom / self.denom > other.nom / other.denom

	# add
	def __add__(self, other):
		nom = self.nom * other.denom + other.nom * self.denom
		denom = self.denom * other.denom
		tmp = Fraction(nom,denom)
		tmp.simplify()
		return tmp

	def simplify(self):
		gcd = greatest_common_divisor(self.nom, self.denom)
		self.nom //= gcd
		self.denom //= gcd


def sorted(lst):

	for i in range(0,len(lst)):
		for j in range(0,len(lst)-i-1):
			if lst[j+1] < lst[j]:
				lst[j], lst[j+1] = lst[j+1], lst[j]

	return lst

if __name__ == '__main__':
	print(sorted([Fraction(5,6),Fraction(22,78),Fraction(22,7),Fraction(7,8),Fraction(9,6),Fraction(15,32)]))
	