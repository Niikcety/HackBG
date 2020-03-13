import sys

def reduce_file_path(path):
	string = path.split('/')
	new_list = []
	for i in string:
		if i == '.' or i == '/':
			continue
		elif i == '..':
			new_list.pop()
		else:
			new_list.append(i)

	new_list = [value for value in new_list if value != '']		
	if new_list == []:
		return '/'
	else:
		string1 = '/'.join(new_list)
		return string1

if __name__ == '__main__':
	print(reduce_file_path('/home//rositsazz///courses/./Programming101-Python/week01/../'))
	print(reduce_file_path("/"))
	print(reduce_file_path("/srv/../"))
	print(reduce_file_path("/srv/www/htdocs/wtf/"))
	print(reduce_file_path("/srv/www/htdocs/wtf"))
	print(reduce_file_path("/srv/./././././"))
	print(reduce_file_path("/etc//wtf/"))
	print(reduce_file_path("/etc/../etc/../etc/../"))
	print(reduce_file_path("//////////////"))
	print(reduce_file_path("/../"))