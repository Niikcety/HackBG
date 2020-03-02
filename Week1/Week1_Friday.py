# Problem 1

def check_anagrams():
	first_word = input("Enter first word: ")
	second_word = input("Enter second word: ")
	first_word_dictionary = {}
	second_word_dictionary = {}
	first_word = first_word.lower()
	second_word = second_word.lower()

	if(len(first_word) != len(second_word)):
		print("NOT ANAGRAMS")

	for i in range(len(first_word)):
		first_word_dictionary[first_word[i]] = first_word.count(first_word[i])
		second_word_dictionary[second_word[i]] = second_word.count(second_word[i])

	if first_word_dictionary == second_word_dictionary:
		print("ANAGRAM")
	else:
		print("NOT ANAGRAMS")


# check_anagrams()

# Problem 2
def int_to_list(number):
	list = []
	while number > 0:
		list.append(number % 10)
		number = number // 10
	return list[::-1]

def size_of_number(number):
	return len(int_to_list(number))

def is_credit_card_valid(number):
	
	if number < 0:
		return "Invalid number."
	if size_of_number(number) % 2 == 0:
		return "Invalid number."


	list = int_to_list(number)
	new_list = []
	for i in range(0, len(list)):
		if i % 2 == 0:
			new_list.append(list[i])
		else:
			new_list.append(list[i]*2)

	print(new_list)
	print(sum(new_list))
	if sum(new_list) % 10 == 0:
		return "Valid Number."
	else:
		return "Invalid number."
	
# print(is_credit_card_valid(79927398713))
# print(is_credit_card_valid(79927398715))


# Problem 3

def list_of_primes(n):
	list_primes = []
	for i in range(2,n):
		if is_it_prime(i):
			list_primes.append(i)
	return list_primes

def is_it_prime(n):
	
	for i in range(2,n):
		
		if n % i == 0:
			return False
	return True

def goldbach(n):
	pass

# print(list_of_primes(97))

# Problem 4
def sum_of_matrix(m):
	sums = 0
	for i in range(0, len(m)):
		for j in range(0, len(m[i])):
			sums += m[i][j]

	return sums

def normalize(m):
	for i in range(0, len(m)):
		for j in range(0, len(m[0])):
			if m[i][j] < 0:
				m[i][j] = 0
	return m

def number_of_neighbours(i,j,r,c,m):
	print(m)
	if i == 0 and j == 0:
		m[1][0] -= m[i][j]
		m[1][1] -= m[i][j]
		m[0][1] -= m[i][j]
		return m 
	if i == 0 and j == c - 1:
		m[0][c-2] -= m[i][j]
		m[1][c-2] -= m[i][j]
		m[1][c-1] -= m[i][j]
		return m
	if i == r -1 and j == c -1:
		m[r-1][c-2] -= m[i][j]
		m[r-2][c-1] -= m[i][j]
		m[r-2][c-2] -= m[i][j]
		return m
	if i == r - 1 and j == 0:
		m[r-2][0] -= m[i][j]
		m[r-2][1] -= m[i][j]
		m[r-1][1] -= m[i][j]
		return m
	if i == 0:
		m[0][j-1] -= m[i][j]	
		m[0][j+1] -= m[i][j]
		m[1][j] -= m[i][j]
		m[1][j-1] -= m[i][j]
		m[1][j+1] -= m[i][j]
		return m
	if i == r -1:
		m[i][j-1] -= m[i][j]
		m[i][j+1] -= m[i][j]
		m[i-1][j] -= m[i][j]
		m[i-1][j-1] -= m[i][j]
		m[i-1][j+1] -= m[i][j]
		return m
	if j == 0:
		m[i-1][j+1] -= m[i][j]
		m[i-1][j] -= m[i][j]
		m[i][j+1] -= m[i][j]
		m[i+1][j+1] -= m[i][j]
		m[i+1][j] -= m[i][j]
		return m
	if j == c-1:
		m[i][j-1] -= m[i][j]
		m[i+1][j] -= m[i][j]
		m[i+1][j-1] -= m[i][j]
		m[i-1][j-1] -= m[i][j]
		m[i-1][j] -= m[i][j]
		return m
	else:
		m[i][j-1] -= m[i][j]
		m[i+1][j] -= m[i][j]
		m[i+1][j-1] -= m[i][j]
		m[i-1][j-1] -= m[i][j]
		m[i-1][j] -= m[i][j]
		m[i][j+1] -= m[i][j]
		m[i+1][j+1] -= m[i][j]
		m[i-1][j+1] -= m[i][j]
		return m

def matrix_bombin_plan(matrix):
	dictionary = {}
	r = len(matrix)
	c = len(matrix[0])
	m = [ele[:] for ele in matrix]
	sum_matrix = sum_of_matrix(matrix)
	for i in range(0,r):
		for j in range(0,c):
			dictionary[(i,j)] = sum_of_matrix(normalize(number_of_neighbours(i,j,r,c,m)))
			m = [ele[:] for ele in matrix]
	print(dictionary)
	


#print(number_of_neighbours(0,0,3,3,[[1,2,3],[4,5,6],[7,8,9]]))
	
matrix_bombin_plan([[1,2,3],
					[4,5,6],
					[7,8,9]])

#[[10,10,10],[10,9,10],[10,10,10]]

# 10 10 10 10
# 10 10 10 10
# 10 10 10 10
# 10 10 10 10