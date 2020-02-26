# Problem 1
def sum_of_digits(n):
	if n < 0:
		n *= -1
	sum = 0
	while n > 0:
		sum += n % 10
		n = n // 10
	return sum

#print(sum_of_digits(1325132435356))

# Problem 2
def to_digits(n):
	string_of_digit = str(n)
	lst = []
	for x in string_of_digit:
		lst.append(x)
	return lst

#print(to_digits(123))

# Problem 3
def to_number(digits):
	smth = ''.join(str(digit) for digit in digits)
	return int(smth)


#print(to_number([122,3,4,5]))

# helper function for Problem 4
def fact_of_a_number(number):
	fact = 1
	for i in range(1,number+1):
		fact *= i
	return fact

# Problem 4
def fact_digits(n):
	sum = 0
	while n > 0:
		sum += fact_of_a_number(n % 10)
		n = n // 10
	return sum

# print(fact_digits(111))
# print(fact_digits(145))
# print(fact_digits(999))

# Problem 5
def palindrome(n):
	full_string = str(n)
	first_half_string = full_string[0:len(full_string)//2]
	second_half_string = full_string[::-1][0:len(full_string)//2]
	return first_half_string == second_half_string

# print(palindrome(121))
# print(palindrome("kapak"))
# print(palindrome("baba"))

#Helper for  Problem 6 and Problem 7
def is_it_vowel(str):
	vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']
	if str in vowels:
		return True
	else:
		return False

# Problem 6
def count_vowels(str):
	sum = 0
	for elem in str:
		if is_it_vowel(elem):
			sum += 1
	return sum

# print(count_vowels("Python"))
# print(count_vowels("grhhh"))

# Problem 7
def is_it_letter(letter):
	if (ord(letter) >= 65 and ord(letter) <= 90) or (ord(letter) >= 97 and ord(letter) <= 122):
		return True
	return False

def count_consonants(string):
	number = 0
	for elem in string:
		if is_it_letter(elem) and is_it_vowel(elem) == False:
			number += 1
	return number

print(count_consonants("Python"))
print(count_consonants("Theistareykjarbunga"))
print(count_consonants("grrrrgh!"))
print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
print(count_consonants("A nice day to code!"))

# Problem 8
def char_histogram(string):
	histogram = {}
	for elem in string:
		histogram[elem] = string.count(elem)
	return histogram

# print(char_histogram("Python!"))
# print(char_histogram("AAAAaaa!!!"))

# Problem 9
def sum_matrix(m):
	summ = 0
	for x in m:
		summ += sum(x)
	return summ

# print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
# print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))

# Problem 10

def nan_expand(times):
	if times == 0:
		return ""
	if times == 1:
		return "Not a Nan"
	else:
		return "Not a " + nan_expand(times -1)

# print(nan_expand(0))
# print(nan_expand(1))
# print(nan_expand(2))
# print(nan_expand(3))

# Problem 11
def is_Prime(n):
	for i in range(2,n):
		if n % i == 0:
			return False
	return True	


def prime_factorization(n):
	number = 2
	power = 0
	tupleS = (number,power)
	lst = []
	while number * number < n:
		while n > 1:
			while n % number == 0:
				n = n // number
				power += 1
			if power != 0:
				lst.append((number,power))
				power = 0
			number += 1
	return lst

# print(prime_factorization(10))
# print(prime_factorization(14))
# print(prime_factorization(356)) 
# print(prime_factorization(89))
# print(prime_factorization(1000))

# Problem 12
def group(lst):
	nested_list = []
	grouped_list = []
	for i in range(len(lst)-1):
		if lst[i] == lst[i+1]:
			nested_list.append(lst[i+1])
		else:
			nested_list.append(lst[i])
			grouped_list.append(nested_list)
			nested_list = []
	nested_list.append(lst[len(lst)-1])
	grouped_list.append(nested_list)
	return grouped_list

# print(group([1, 1, 1, 2, 3, 1,1]))
# print(group([1,2,1,2,3,3]))
# print(group([1,2,3]))
# print(group([1,1,1,3,3,3,4,4,5,6,9,1,1,1]))
# Problem 13

def max_consecutive(items):
	list_of_times = []
	number = 1
	for i in range(len(items)-1):
		if items[i] == items[i+1]:
			number += 1
		else:
			list_of_times.append(number)
			number = 1
	list_of_times.append(number)
	return max(list_of_times)


# print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
# print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
# print(max_consecutive([1,2,1,1,1,1,1,9,9,2,2]))

# Problem 14
def word_counter(table):
	pass