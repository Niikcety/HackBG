#Problem 1

def gas_stations(distance, tank_size, stations):
	multiplier = 1
	lst = [] 
	nested_list = []
	for i in stations:
		if i < tank_size * multiplier:
			nested_list.append(i)
		else:
			lst.append(nested_list)
			multiplier += 1
			nested_list = []
			nested_list.append(i)
	lst.append(nested_list)
	lst = [max(i) for i in lst]
	if max(lst) < distance - tank_size:
		print("There wouldn't be enough gas to finish the route")
	else:
		return lst


#Problem 2

def number_sum(number):
	sum = 0
	while number > 0:
		sum += number % 10
		number = number // 10
	return sum

def is_number_balanced(number):
	number_in_str = str(number)
	if number < 10:
		return True
	if len(number_in_str) % 2 == 0:
		first_half = number_in_str[0:len(number_in_str)//2]
		second_half = number_in_str[len(number_in_str)//2:len(number_in_str)]
		return number_sum(int(first_half)) == number_sum(int(second_half))
	else:
		first_half = number_in_str[0:len(number_in_str)//2]
		second_half = number_in_str[len(number_in_str)//2 + 1:len(number_in_str)]
		return number_sum(int(first_half)) == number_sum(int(second_half))

# print(is_number_balanced(9))
# print(is_number_balanced(4518))
# print(is_number_balanced(28471))
# print(is_number_balanced(1238033))		




# Problem 3

def increasing(seq):
	for i in range(len(seq)-1):
		if seq[i] >=  seq[i+1]:
			return False
	return True

def decreasing(seq):
	for i in range(len(seq)-1):
		if seq[i] <= seq[i+1]:
			return False
	return True

def increasiong_or_decreasing(seq):
	if increasing(seq) == True:
		return "Up"
	elif decreasing(seq) == True:
		return "Down"
	else:
		return False

# print(increasiong_or_decreasing([1,2,3,4,5]))
# print(increasiong_or_decreasing([5,6,-19]))
# print(increasiong_or_decreasing([1,1,1,1]))
# print(increasiong_or_decreasing([9,8,7,6]))

# Problem 4
def is_it_palindrome(number):
	return str(number) == str(number)[::-1]


def get_largest_palindrome(n):
	for i in range(n-1, 1, -1):
		if is_it_palindrome(i):
			return i

# print(get_largest_palindrome(99))
# print(get_largest_palindrome(252))
# print(get_largest_palindrome(994687))
# print(get_largest_palindrome(754457))

# Problem 5

def is_it_number(numb):
	if ord(numb) >= 48 and ord(numb) <= 57:
		return True
	return False

def sum_of_numbers(input_string):
	sum1 = 0
	lst = []
	for elem in input_string:
		if is_it_number(elem):
			lst.append(elem)
		else:
			if lst != []:
				lst_string = ''.join(lst)
				sum1 += int(lst_string)
				lst_string = ''
				lst = []
	if lst !=  []:
		lst_string = ''.join(lst)
		sum1 += int(lst_string)
	return sum1

# print(sum_of_numbers("ab125cd3"))
# print(sum_of_numbers("ab12"))
# print(sum_of_numbers("ab"))
# print(sum_of_numbers("1101"))
# print(sum_of_numbers("11110"))
# print(sum_of_numbers("1abc33xyz22"))
# print(sum_of_numbers("0hfabnek"))

# Problem 6
def birthday_ranges(birthdays, ranges):
	numbers = []
	for i in ranges:
		(start,end) = i
		if (start > end) or start <= 0 or start > 365 or end <= 0 or end > 365:
			print("Number out of scope")
			return
		else:
			sum1 = 0
			for j in birthdays:
				if j <= 0 or j > 365:
					print("Number out of scope")
					return
				else:
					if j >= start and j  <= end:
						sum1 += 1
			numbers.append(sum1)

	return numbers

# print(birthday_ranges([-1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
# print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))