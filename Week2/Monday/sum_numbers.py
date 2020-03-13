import sys

def sum_numbers(file_name):
	file = open(file_name,"r")
	string = [] 
	string.append(file.read())
	summ = 0
	lst = []
	for i in range(0,len(string[0])):
		if string[0][i] == ' ':
			string1 = ''.join(lst)
			summ += int(string1)
			lst = []
		else:
			lst.append(string[0][i])
			
	string1 = ''.join(lst)
	summ += int(string1)

	return summ 

	

if __name__ == '__main__':
	print(sum_numbers(sys.argv[1]))